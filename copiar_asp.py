import os
import shutil


def copiar_asp_para_pastas():
    arquivo_origem = "asp.py"
    if not os.path.exists(arquivo_origem):
        print(f"Arquivo '{arquivo_origem}' não encontrado.")
        return

    pastas = [p for p in os.listdir() if os.path.isdir(p)
              ]  # Lista apenas diretórios

    for pasta in pastas:
        destino = os.path.join(pasta, "asp.py")
        shutil.copy2(arquivo_origem, destino)  # Copia mantendo metadados
        print(f"Arquivo '{arquivo_origem}' copiado para '{pasta}/'.")


if __name__ == "__main__":
    copiar_asp_para_pastas()
