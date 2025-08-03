# -*- coding: utf-8 -*-
import os
import shutil
import time

# --- CONFIGURAÇÃO ---
# ATENÇÃO: Altere o caminho abaixo para a sua pasta de Downloads ou a pasta que deseja organizar.
# Exemplo para Windows: "C:/Users/SeuUsuario/Downloads"
# Exemplo para macOS/Linux: "/Users/SeuUsuario/Downloads"
PASTA_PARA_ORGANIZAR = "D:/arthu/Downloads" 

# Dicionário que mapeia os nomes das pastas para as extensões de arquivo correspondentes.
# Você pode personalizar isso, adicionando ou removendo extensões e pastas.
DIRS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt"],
    "Planilhas": [".csv", ".xls", ".xlsx"],
    "Videos": [".mov", ".mp4", ".avi", ".mkv", ".wmv"],
    "Musicas": [".mp3", ".wav", ".ogg", ".flac"],
    "Arquivos Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executaveis": [".exe", ".msi", ".dmg"],
    "Outros": [] # Uma pasta para tudo que não se encaixar nas categorias acima
}

def organizar_pasta(caminho_pasta):
    """
    Organiza os arquivos na pasta especificada, movendo-os para subdiretórios
    baseado em suas extensões.
    """
    print(f"Iniciando organização da pasta: {caminho_pasta}\n")
    
    # Lista todos os arquivos e pastas no diretório especificado
    try:
        lista_de_arquivos = os.listdir(caminho_pasta)
    except FileNotFoundError:
        print(f"ERRO: A pasta '{caminho_pasta}' não foi encontrada.")
        print("Por favor, verifique o caminho na variável 'PASTA_PARA_ORGANIZAR' e tente novamente.")
        return

    arquivos_movidos = 0

    # Itera sobre cada item na pasta
    for arquivo in lista_de_arquivos:
        caminho_completo_arquivo = os.path.join(caminho_pasta, arquivo)

        # Verifica se o item é um arquivo (e não uma pasta)
        if os.path.isfile(caminho_completo_arquivo):
            # Separa o nome do arquivo de sua extensão
            nome_arquivo, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower() # Converte a extensão para minúsculas

            pasta_destino = None

            # Procura a pasta de destino correta com base na extensão
            for pasta, extensoes in DIRS.items():
                if extensao in extensoes:
                    pasta_destino = pasta
                    break
            
            # Se a extensão não foi encontrada em nenhuma lista, usa a pasta "Outros"
            if pasta_destino is None:
                pasta_destino = "Outros"

            # Cria o caminho completo para a pasta de destino
            caminho_pasta_destino = os.path.join(caminho_pasta, pasta_destino)

            # Cria a pasta de destino se ela ainda não existir
            os.makedirs(caminho_pasta_destino, exist_ok=True)

            # Cria o caminho completo para o arquivo no novo local
            novo_caminho_arquivo = os.path.join(caminho_pasta_destino, arquivo)

            # Move o arquivo para a pasta de destino
            try:
                shutil.move(caminho_completo_arquivo, novo_caminho_arquivo)
                print(f"Movido: '{arquivo}' -> para a pasta '{pasta_destino}'")
                arquivos_movidos += 1
            except Exception as e:
                print(f"Erro ao mover '{arquivo}': {e}")
    
    print(f"\nOrganização concluída! {arquivos_movidos} arquivo(s) movido(s).")


# --- EXECUÇÃO DO SCRIPT ---
if __name__ == "__main__":
    organizar_pasta(PASTA_PARA_ORGANIZAR)
