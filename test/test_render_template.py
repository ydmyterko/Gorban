from pdf_from_template import *
from read_pdf import *


# згенерувати пдф:
#render_template("шлях до файлу шаблону з папки ресурсів", "шлях до файлу значень", "шлях до згенерованого пдф файла")
result_pdf = template_pdf('resource/tmpl_1_val_1.json', 'resource/template_1.tmpl', 'result.pdf')

# прочитати пдф
# pdf_content = read_pdf("шлях до згенерованого пдф файла")
pdf_content = read_pdf('result.pdf')

# assert pdf_content == "тут те що ти очікуєш щоб було в результаті"
expected_content = "Expected result"

# Test 1 - compare lines
if pdf_content != expected_content:
    print ('files are different')
else:
    print('files are same')

#Test 2 - check if name_from is 'Dmytrovych'
#Test 3 - check if name_to is 'valentina nappy'
#Test 4 - check if datetime is 'now'
#Test 5 - check if