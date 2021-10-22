# importing required modules
import argparse
import PyPDF2

class ReadPDF:
    def __init__(self, output):
        print('--- ReadPDF ---')
        self.output = str(output)

    def content(self):
        print('--- open PDF ---')
        pdfFileObj = open(self.output, 'rb')

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