import PyPDF2
import os
os.system('cls')

pdf = open('C:\\contar_pdf\\0812040108.pdf' , 'rb')
testa = PyPDF2.PdfFileReader(pdf)
print(testa.numPages)