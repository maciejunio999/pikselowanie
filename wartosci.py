hz, wz = 1480, 1120
piksel = 40
for i in range(0, hz, piksel):
    l = []
    for j in range(0, wz, piksel):
        l.append(str(i) + " " + str(j))
    #print(l)


from PIL import Image

im = Image.open(r"jaa.jpg")
im = Image.open(r"jaa.jpg")
pixels = im.load()
print(len(pixels))



