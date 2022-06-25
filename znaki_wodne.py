from PIL import Image, ImageDraw, ImageFont

im = Image.open('jan.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "Pedal"

font = ImageFont.load("Arial")

font = ImageFont.truetype('Arial', 20)
textwidth, textheight = draw.textsize(text, font)

# calculate new x,y coordinates of the text
x = (width - textwidth)/2
y = (height - textheight)/2

# draw watermark in the center
draw.text((x, y), text, font=font)

im.show()