import argparse
from pdf_from_template import TemplatePDF

parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--values")
parser.add_argument("--template")
parser.add_argument("--output")

args = parser.parse_args()
values = args.values
template = args.template
output = args.output

print(values)
print(template)
print(output)

my_PDF = TemplatePDF(values, template, output)
my_PDF.area()
