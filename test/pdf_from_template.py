import json
from fpdf import FPDF

def template_pdf(values, template, output):
  print("-- Class TemplatePDF --")
  print(values)
  print(template)
  print(output)

  print('--- Reading Template file---')
  with open(template) as file:
    template_str = file.read()
  print(template_str)

  print('--- Reading JSON file---')
  with open(values) as f:
    data = json.load(f)
    print(data)

  pairs = data.items()
  for key, value in pairs:
    print(key,value)
    template_str = template_str.replace("{" + key + "}",value)

  print('--- creating PDF ---')
  pdf = FPDF()
  pdf.add_page()
  pdf.set_font('Arial', 'B', 10)

  # Adding JSON text
  print('--- Adding JSON text ---')
  pdf.multi_cell(110, 5, txt=str(template_str))

  # Creating output
  print('--- Creating output ---')
  pdf.output(output, 'F')