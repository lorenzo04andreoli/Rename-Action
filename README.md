# 📄 Renomeador Automático de PDFs por Nome (OCR Inteligente)

Este projeto automatiza o processo de **renomear arquivos PDF escaneados** com base no nome da pessoa que consta no documento, como por exemplo:

```
Comparecimento de João da Silva.pdf
```

O script extrai o **texto diretamente do PDF**, identifica o nome próximo à linha `RG:` e renomeia os arquivos de forma padronizada.

---

## 🧠 Funcionalidades

- ✅ Lê PDFs escaneados contendo termos de comparecimento.
- ✅ Extrai nomes automaticamente com base no texto visível no PDF.
- ✅ Corrige erros comuns de OCR (ex: "1 Fulano", "f Maria").
- ✅ Cobre múltiplas variações de posicionamento do nome (antes ou depois do RG).
- ✅ Gera arquivos com nomes limpos e prontos para organização.
- ✅ Pode ser adaptado para qualquer tipo de documento com pequenas alterações.

---

## 📁 Estrutura de Pastas

```
📂 raiz/
├── pdfs/             → coloque aqui os arquivos PDF escaneados
├── renomeados/       → arquivos renomeados serão movidos para cá
├── renomear.py       → script principal
└── README.md         → este arquivo
```

---

## ⚙️ Requisitos

- Python 3.8 ou superior
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io)
- Biblioteca `re` (Regex, já vem com Python)

### 📦 Instalar dependências:

```bash
pip install pymupdf
```

---

## ▶️ Como usar

1. Coloque todos os PDFs escaneados na pasta `pdfs/`.
2. Execute o script:

```bash
python renomear.py
```

3. Os arquivos com nome extraído serão movidos para a pasta `renomeados/` com nomes como:

```
Comparecimento de Maria da Silva.pdf
```

---

## 🧪 Teste de Extração de Texto

Caso algum PDF não seja renomeado corretamente, você pode usar o script `test.py` para inspecionar o texto real que está dentro do arquivo:

### 📄 `test.py`

```python
import fitz  # PyMuPDF

# Altere o caminho abaixo para o PDF que deseja testar
arquivo = Path("pdfs/seu_arquivo_aqui.pdf")

with fitz.open(arquivo) as doc:
    for i in range(len(doc)):
        texto = doc[i].get_text()
        print(f"Página {i + 1}:\n{texto}\n{'-'*50}")
```

Esse teste ajuda a identificar se o nome realmente está presente e legível no conteúdo textual extraído pelo PyMuPDF.

---

## ❗️ Observações

- O script não usa OCR de imagem — ele extrai texto diretamente dos PDFs. Isso torna o processo muito mais rápido e preciso.
- Certifique-se de que o PDF realmente contém **texto selecionável**. Se o PDF for pura imagem (como foto), será necessário OCR com Tesseract (não incluso aqui).

---

## 📌 Melhorias futuras

- Interface gráfica (GUI)
- Log com erros detalhados
- Suporte a outras estruturas de documentos (ex: certidões, termos de audiência)

---

## 🧑‍💻 Autor

**Lorenzo**  
📍 Paranaguá, PR  
🚀 Desenvolvedor e automador de tarefas repetitivas

---

## 🪪 Licença

Este projeto é de uso livre, pessoal ou profissional. Você pode copiar, adaptar e distribuir à vontade.