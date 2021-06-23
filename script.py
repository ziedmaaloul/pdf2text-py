import sys, getopt, argparse
import pdftotext
parser = argparse.ArgumentParser()
parser.add_argument('--inputFile', type=str)
parser.add_argument('--outputFolder', type=str)
args = parser.parse_args()
inputfile = args.inputFile
outputfile = args.outputFolder
#output = outputfile + "/data.json" 
# Load your PDF
with open(inputfile, "rb") as f:
    pdf = pdftotext.PDF(f)



# Read some individual pages
output = open(outputfile+"/test.txt", "w")

#with open(output, 'w') as ofile:
for p in pdf:
    print(p)
    #ofile.writelines(str(p))
