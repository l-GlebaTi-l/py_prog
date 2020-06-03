from PIL import Image1, Image2 , ImageDraw
inp=input().split()
try:
    image_inp1=inp[0]
except:
    image_inp1="cheba.jpg"
try:
    image_inp2=inp[1]
except:
    image_inp2="krok.jpg"
try:
    image_out=inp[2]
except:
    image_out="nechto.jpg"
try:
    image1=Image1.open(image_inp1)
except:
    print ("No first file")
try:
    image2=Image2.open(image_inp2)
except:
    print ("No second file")
else:
    draw=ImageDraw.Draw(image1)
    pix1=image1.load()
    pix2=image2.load()
    for i in range (image1.size[0]):
        for j in range (image1.size[1]):
            p1 = (pix1[i,j][0] + pix1[i,j][1] + pix1[i,j][2]) / 3
            p2 = (pix2[i,j][0] + pix2[i,j][1] + pix2[i,j][2]) / 3

	    a = pix[i,j][0] * p2 / p1
	    b = pix[i,j][1] * p2 / p1
	    c = pix[i,j][2] * p2 / p1
            draw.point((i,j),(a,b,c))
    image.save(image_out,"jpeg")

    image.show()   