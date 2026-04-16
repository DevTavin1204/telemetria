import csv
import os
import uuid
from decimal import Decimal
from datetime import datetime

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import transaction, connection

from telemetria.models import MedicaoVeiculoTemp, Veiculo, Medicao


# Esta função executa uma procedure no banco de dados após
# a importação do arquivo CSV. O parâmetro "arquivoid"
# identifica quais registros da tabela temporária devem ser processados.

def executar_procedure_pos_importacao(arquivoid):

    with connection.cursor() as cursor:

        # Executa a procedure "processa_arquivo"
        # enviando o identificador do arquivo importado
        cursor.callproc("processa_arquivo", [arquivoid])


# Esta função recebe o arquivo CSV enviado pelo usuário,
# valida seus dados, armazena em uma tabela temporária
# e executa uma procedure caso a importação seja bem-sucedida.

def processar_csv_medicoes(arquivo):

    # Gera um identificador único para o arquivo importado
    arquivoid = str(uuid.uuid4())


    # Define o diretório onde o arquivo será salvo e cria
    # a pasta caso ela ainda não exista.

    pasta_destino = os.path.join(settings.MEDIA_ROOT, "importacoes_medicao")
    os.makedirs(pasta_destino, exist_ok=True)

    # Define nome único para evitar conflitos de arquivos
    nome_salvo = f"{arquivoid}_{arquivo.name}"

    # Salva o arquivo fisicamente no servidor
    fs = FileSystemStorage(location=pasta_destino)
    nome_arquivo_salvo = fs.save(nome_salvo, arquivo)

    # Caminho completo do arquivo salvo
    caminho_completo = os.path.join(pasta_destino, nome_arquivo_salvo)


    # Variáveis utilizadas para controle do processamento.

    total_linhas_arquivo = 0
    erros = []
    linhas_para_inserir = []

    # Cria um cache em memória com veículos e medições
    # para evitar múltiplas consultas ao banco e melhorar performance.

    veiculos_cache = {v.id: v for v in Veiculo.objects.all()}
    medicoes_cache = {m.id: m for m in Medicao.objects.all()}


    # Abre o arquivo salvo e realiza leitura linha por linha.

    with open(caminho_completo, mode="r", encoding="utf-8-sig", newline="") as f:

        reader = csv.DictReader(f, delimiter=';')


        # Verifica se o arquivo possui os campos obrigatórios.

        campos_esperados = {"veiculoid", "medicaoid", "data", "valor"}

        if not reader.fieldnames:
            raise Exception("O CSV não possui cabeçalho.")

        if not campos_esperados.issubset(set(reader.fieldnames)):
            raise Exception(
                f"Cabeçalho inválido. Esperado: {list(campos_esperados)}. Recebido: {reader.fieldnames}"
            )



        # Percorre cada linha do arquivo realizando validações
        # e preparando registros válidos para inserção.

        for numero_linha, row in enumerate(reader, start=2):

            total_linhas_arquivo += 1

            try:

                # Converte os dados recebidos e valida existência
                # dos relacionamentos no banco.

                id_veiculo = int(row["veiculoid"])
                id_medicao = int(row["medicaoid"])

                veiculo = veiculos_cache.get(id_veiculo)
                if not veiculo:
                    raise Exception(f"Veículo {id_veiculo} não encontrado.")

                medicao = medicoes_cache.get(id_medicao)
                if not medicao:
                    raise Exception(f"Medição {id_medicao} não encontrada.")

                data_convertida = datetime.strptime(
                    row["data"].strip(),
                    "%Y-%m-%d %H:%M:%S"
                )

                valor_convertido = Decimal(row["valor"].strip())


                # Cria objetos da tabela temporária para inserção em lote.

                linhas_para_inserir.append(
                    MedicaoVeiculoTemp(
                        veiculo=veiculo,
                        medicao=medicao,
                        data_hora=data_convertida,
                        valor=valor_convertido,
                        arquivoid=arquivoid
                    )
                )


            # Caso ocorra erro em alguma linha, ele será armazenado
            # sem interromper o processamento do restante do arquivo.

            except Exception as e:

                erros.append({
                    "linha": numero_linha,
                    "erro": str(e)
                })


    # Conta quantas linhas passaram na validação.

    total_linhas_validas = len(linhas_para_inserir)

    # Realiza inserção segura utilizando transação para evitar
    # inconsistência em caso de erro.

    with transaction.atomic():

        if linhas_para_inserir:

            MedicaoVeiculoTemp.objects.bulk_create(
                linhas_para_inserir,
                batch_size=1000
            )

        # Verifica se todas as linhas válidas foram realmente inseridas.

        total_linhas_importadas = MedicaoVeiculoTemp.objects.filter(
            arquivoid=arquivoid
        ).count()

        quantidades_conferem = total_linhas_validas == total_linhas_importadas


        # Executa a procedure se tudo estiver correto.
        # Caso contrário remove os dados inseridos.

        if quantidades_conferem:

            executar_procedure_pos_importacao(arquivoid)

        else:

            MedicaoVeiculoTemp.objects.filter(
                arquivoid=arquivoid
            ).delete()

    # Retorna um resumo completo da execução da importação.

    return {
        "arquivoid": arquivoid,
        "arquivo_salvo": nome_arquivo_salvo,
        "caminho": caminho_completo,
        "total_linhas_arquivo": total_linhas_arquivo,
        "total_linhas_importadas": total_linhas_importadas,
        "quantidades_conferem": total_linhas_arquivo == total_linhas_importadas,
        "erros": erros
    }
