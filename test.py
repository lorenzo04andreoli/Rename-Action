import fitz

# Altere o caminho abaixo para o PDF que deseja testar
arquivo = r"pdfs\Seu-arquivo.pdf"

with fitz.open(arquivo) as doc:
    for i in range(len(doc)):
        texto = doc[i].get_text()
        print(f"Página {i + 1}:\n{texto}\n{'-'*50}")