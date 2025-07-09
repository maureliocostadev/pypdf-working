import fitz  # PyMuPDF
import shutil

pdf_names = ['pll','link_control_fly']
path_move = 'Flying-Start/Specifications/uploads/'
for pdf_name in pdf_names:
    # Caminho do arquivo PDF
    pdf_path = f"{path_move}{pdf_name}.pdf"
    # Abrir o PDF
    pdf_document = fitz.open(pdf_path)
    #Converter cada página para PNG
    page = pdf_document[0]
    pix = page.get_pixmap()
    pix.save(f"{pdf_name}.png")  # Salva cada página como PNG
    arquivo_origem = f"{pdf_name}.png"
    pasta_destino = path_move  # Certifique-se de que a pasta existe
    shutil.move(arquivo_origem, pasta_destino)





print("Conversão concluída!")
