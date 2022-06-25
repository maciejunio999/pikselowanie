import math
from PIL import Image, ImageGrab

zdj = Image.open(r"jaa.jpg")

rgb = ImageGrab.grab().load()[1, 1]
rgbz = [181, 42, 111]

pixels = zdj.load()
width, height = zdj.size

for y in range(40, 100):  # iteracja po rzędach
    for x in range(40, 100):  # iteracja po kolumnach
        zdj.putpixel((y, x), tuple(rgbz))

zdj.show()

