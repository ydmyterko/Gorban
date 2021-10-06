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
    with open(self.values) as f:
      data = json.load(f)
      print(data)

    json_str=""
    item_cnt=0
    pairs = data.items()
    for key, value in pairs:
      item_cnt+= 1
      print(key,value)
      json_str += str(item_cnt) + ". " + str(key) + " - " + str(value) + "\n"

    # Reading Template file
    with open(self.template) as file:
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
    pdf.output(self.output, 'F')


