import pytesseract as tess
from PIL import Image

img = Image.open('my_images/20200313-134608_Android_Flask_0.jpg')
text = tess.image_to_string(img)

print(text)
