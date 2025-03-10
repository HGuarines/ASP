import os


def criar_pastas_q1_q25():
    for i in range(1, 26):
        nome_pasta = f"Q{i}"
        os.makedirs(nome_pasta, exist_ok=True)
        print(f"Pasta '{nome_pasta}' criada com sucesso.")


if __name__ == "__main__":
    criar_pastas_q1_q25()
