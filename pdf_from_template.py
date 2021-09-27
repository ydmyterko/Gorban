import json
from fpdf import FPDF

class TemplatePDF:

  def __init__(self, values, template, output):
    self.values = str(values)
    self.template = str(template)
    self.output=str(output)

    print("-- Class TemplatePDF --")
    print(self.values)
    print(self.template)
    print(self.output)

  def area(self):
    # Reading JSON file
    optionStr=''

    with open(self.values) as f:
      data = json.load(f)
      print(data)

    for p in data:
       optionStr += p['model'] + " - " + p['prise'] + "\n"

    print(optionStr)

    # Reading Template file
    with open(self.template) as file:
      templateStr = file.read()
    print(templateStr)

    # total string
    totalStr = templateStr  + optionStr
    print(totalStr)

    # creating PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 10)

    # Adding JSON text
    pdf.multi_cell(100, 10, txt=str(totalStr))

    # Creating output
    pdf.output(self.output, 'F')


