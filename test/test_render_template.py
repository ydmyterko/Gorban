from pdf_from_template import *
from read_pdf import *

# згенерувати пдф:
#render_template("шлях до файлу шаблону з папки ресурсів", "шлях до файлу значень", "шлях до згенерованого пдф файла")
result_pdf = TemplatePDF('resource/tmpl_1_val_1.json', 'resource/template_1.tmpl', 'result.pdf')
result_pdf.area()

# прочитати пдф
# pdf_content = read_pdf("шлях до згенерованого пдф файла")
pdf_content = ReadPDF('result.pdf')
pdf_content.content()

# assert pdf_content == "тут те що ти очікуєш щоб було в результаті"
pdf_content = "Expected result"