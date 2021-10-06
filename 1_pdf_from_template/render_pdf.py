import argparse
from pdf_from_template import TemplatePDF
import json
from fpdf import FPDF

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--values")
parser.add_argument("--template")
parser.add_argument("--output")

args = parser.parse_args()
values = args.values
template = args.template
output = args.output

values = "values.json"
template = "template.tmpl"
output = "result.pdf"

print(values)
print(template)
print(output)

with open(values) as f:
    data = json.load(f)
    print(data)

json_str = ""
item_cnt = 0
pairs = data.items()
for key, value in pairs:
    item_cnt += 1
    print(key, value)
    json_str += str(item_cnt) + ". " + str(key) + " - " + str(value) + "\n"

# Reading Template file
with open(template) as file:
    template_str = file.read()
print(template_str)

# total string
total_str = template_str + str(json_str)
print(total_str)

# creating PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 10)

# Adding JSON text
pdf.multi_cell(110, 5, txt=str(total_str))

# Creating output
pdf.output(output, 'F')



