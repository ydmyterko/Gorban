# importing required modules
import argparse
import PyPDF2

# creating a pdf file object
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--pdfname")

args = parser.parse_args()
pdf_name = args.pdfname
#pdf_name = "result.pdf"

pdfFileObj = open(pdf_name, 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()