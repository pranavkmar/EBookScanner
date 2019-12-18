import pytesseract as tess
from PIL import Image

img = Image.open('tests/data/OCR_Test/Screenshot_20191218_141218.png')
text = tess.image_to_string(img)

print(text)
