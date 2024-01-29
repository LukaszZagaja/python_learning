from PIL import Image


print('\n')
mac = Image.open('example.jpg')
#print(type(mac))
#print(mac.size)
#print(mac.filename)
#print(mac.format_description)

###-------CROPPING IMAGES------------###
pencils = Image.open('pencils.jpg')
# pencils.show()
#print(pencils.size)

x = 0 
y = 0
w = 1950/3
h = 1300/10
pen_crop = pencils.crop((x,y,w,h))
#pen_crop.show()


##---Cropping from the bottom
x = 0
y = 1100
w = 1950 / 3
h = 1300
#pencils.crop((x,y,w,h)).show()

##---Cropping only mac
#print(mac.size)
halfway = 1993 / 2
x = halfway - 200
w = halfway + 200
y = 800
h = 1257
computer = mac.crop((x,y,w,h))

###------------- PASTING IMAGES ----------------###
mac.paste(im=computer, box=(0,0)) # can change numbers multiple times in 1 line to paste it multiple times in given image 
#mac.show()

###--------- RESIZING -----------###
#print(mac.size)
#mac.resize((3000,500))
#mac.show()

###--------- ROTATING -----------###
#mac.rotate(90)
#mac.show()
