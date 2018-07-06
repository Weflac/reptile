
import pytesseract
import os
from PIL import Image

# base_dir = os.path.abspath('static/tess2.jpg')
# print(os.path.abspath('static/tess2.jpg'))


image = Image.open('tess2clean.png')
text = pytesseract.image_to_string(image)

print(text)

