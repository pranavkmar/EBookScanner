# *** Convert images files to pdf file.***
from os import listdir
from fpdf import FPDF

# get the path of images
path = "/home/sit/PycharmProjects/BookScannerDemoRasp/tests/data/PDF_renderTest/"

# get list of all images
imagelist = listdir(path)

# create an A4-size pdf document
pdf = FPDF('P', 'mm', 'A4')

x, y, w, h = 0, 0, 200, 250

for image in imagelist:
    pdf.add_page()
    pdf.image(path + image, x, y, w, h)

pdf.output("images.pdf", "F")
