import os
import re
import fitz 
from datetime import datetime

data=datetime.today().strftime('%m.%Y')

PASTA_PDFS = 'pdfs'
PASTA_RENOMEADOS = 'renomeados'

os.makedirs(PASTA_RENOMEADOS, exist_ok=True)

def limpar_nome(nome):
    nome = nome.replace('\n', ' ').replace('\r', ' ')
    nome = re.sub(r'\s+', ' ', nome).strip()
    nome = re.sub(r'[<>:"/\\|?*]', '', nome)
    return nome

def extrair_nome(texto):
    """
    Extrai o nome próximo de 'RG:' (até 2 linhas acima e 1 abaixo), corrigindo erros comuns de OCR.
    """
    linhas = texto.splitlines()
    for i, linha in enumerate(linhas):
        if 'RG:' in linha.upper():
            candidatos = []

            if i + 1 < len(linhas):
                candidatos.append(linhas[i + 1].strip())
            if i - 1 >= 0:
                candidatos.append(linhas[i - 1].strip())
            if i - 2 >= 0:
                candidatos.append(linhas[i - 2].strip())

            for nome in candidatos:
                # Remove prefixos inválidos (números, letras soltas, símbolos)
                nome = re.sub(r'^[^A-Za-zÁÉÍÓÚÂÊÔÃÕÇáéíóúâêôãõç]+', '', nome)
                nome = re.sub(r'^[a-zA-Z]\s+', '', nome)  # remove "f ", "r ", etc.

                # Confirma que é um nome: pelo menos 2 palavras com letras
                palavras = nome.split()
                if len(palavras) >= 2 and all(len(p) > 1 for p in palavras):
                    nome = re.sub(r'\s+', ' ', nome).strip()
                    return nome.title()

    return None



def extrair_texto_pdf(caminho_pdf):
    texto_completo = ''
    with fitz.open(caminho_pdf) as pdf:
        for pagina in pdf:
            texto_completo += pagina.get_text()
    return texto_completo

def renomear_pdfs():
    for arquivo in os.listdir(PASTA_PDFS):
        if arquivo.lower().endswith('.pdf'):
            caminho_pdf = os.path.join(PASTA_PDFS, arquivo)
            print(f'Processando: {arquivo}')
            
            texto = extrair_texto_pdf(caminho_pdf)
            nome = extrair_nome(texto)
            
            if nome:
                nome_limpo = limpar_nome(nome)
                novo_nome_base = f'Comparecimento de {nome_limpo} {data}'
                novo_nome = f'{novo_nome_base}.pdf'
                caminho_novo = os.path.join(PASTA_RENOMEADOS, novo_nome)

                contador = 1
                while os.path.exists(caminho_novo):
                    novo_nome = f'{novo_nome_base} ({contador}).pdf'
                    caminho_novo = os.path.join(PASTA_RENOMEADOS, novo_nome)
                    contador += 1
                
                os.rename(caminho_pdf, caminho_novo)
                print(f'✔️ Renomeado para: {novo_nome}')
            else:
                print(f'❗ Nome não encontrado em: {arquivo}')

if __name__ == '__main__':
    renomear_pdfs()
