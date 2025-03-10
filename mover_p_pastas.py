import os
import shutil


def mover_arquivos_para_pastas():
    # Lista apenas arquivos no diretório atual
    arquivos = [f for f in os.listdir() if os.path.isfile(f)]

    for arquivo in arquivos:
        # Obtém o nome do arquivo sem extensão
        nome_base = arquivo.split('.')[0]

        # Verifica se segue o padrão "Qx"
        if nome_base.startswith("Q") and nome_base[1:].isdigit():
            pasta_destino = nome_base  # Nome da pasta correspondente

            if os.path.exists(pasta_destino):  # Verifica se a pasta existe
                shutil.move(arquivo, os.path.join(pasta_destino, arquivo))
                print(f"Arquivo '{arquivo}' movido para '{pasta_destino}/'.")
            else:
                print(
                    f"Pasta '{pasta_destino}' não encontrada. Arquivo '{arquivo}' não movido.")


if __name__ == "__main__":
    mover_arquivos_para_pastas()
