arquivos=("documentos.pdf", "foto.jpg", "relatorio.pdf", "relatorio.xlsx")
contagem_pdf = sum(1 for arquivo in arquivos if arquivo.endswith(".pdf"))
print(contagem_pdf)