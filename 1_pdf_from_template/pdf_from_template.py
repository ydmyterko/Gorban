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
    option_str=''

    with open(self.values) as f:
      data = json.load(f)
      print(data)

    for p in data:
        print(p)
        pairs = p.items()
        line=""
        for key, value in pairs:
          line += value + " "
        option_str += line + "\n"
        print(option_str)

    # Reading Template file
    with open(self.template) as file:
      template_str = file.read()
    print(template_str)

    # total string
    total_str = template_str  + option_str
    print(total_str)

    # creating PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 10)

    # Adding JSON text
    pdf.multi_cell(100, 10, txt=str(total_str))

    # Creating output
    pdf.output(self.output, 'F')


