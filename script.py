import sys, getopt, argparse
import pdfplumber
import os
parser = argparse.ArgumentParser()
parser.add_argument('--inputFile', type=str)
parser.add_argument('--outputFolder', type=str)
args = parser.parse_args()
inputfile = args.inputFile
outputfile = args.outputFolder
pdf = pdfplumber.open(inputfile)
page = pdf.pages[0]
text = page.extract_text()
pdf.close()
text_file = open(outputfile+"/data.txt", "w")
n = text_file.write(text)
text_file.close()