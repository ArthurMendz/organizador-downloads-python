# organizador-downloads-python
Um script em Python que organiza arquivos em uma pasta com base em suas extensões

# 📂 Organizador de Downloads em Python

Um script simples e eficiente que organiza automaticamente os arquivos em uma pasta (como a de Downloads), movendo-os para subdiretórios específicos com base em suas extensões.

## 🚀 Como Funciona

O script verifica todos os arquivos na pasta especificada. Para cada arquivo, ele identifica a extensão (ex: `.pdf`, `.jpg`, `.zip`) e o move para uma pasta correspondente (ex: "Documentos", "Imagens", "Arquivos Compactados"). Se a pasta de destino não existir, o script a cria automaticamente.

## 🛠️ Como Usar

1.  Faça o download do arquivo `organizador_downloads_py.py`.
2.  Abra o arquivo em um editor de texto e altere a variável `PASTA_PARA_ORGANIZAR` para o caminho da pasta que você deseja organizar.
3.  Execute o script através do terminal:
    ```bash
    python organizador_downloads_py.py
    ```
4.  Pronto! Sua pasta será organizada em segundos.

## 💻 Tecnologias Utilizadas

* **Python 3**
* Módulos Nativos: `os` e `shutil`
