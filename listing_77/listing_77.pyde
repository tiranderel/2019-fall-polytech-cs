img1 =None
img2 =None

def setup ():
    global img1, img2
    background (100) 
    smooth ()
    img1 = loadImage ("CR1.jpg")
    img2 = loadImage ("CR2.jpg")
    size (784 , 600)

def draw ():
    global img1, img2
    myTintBO = map (mouseX , 0, width , 0, 255) 
    myTintVP = map (mouseX , 0, width , 255 , 0)
    tint (255 , myTintVP )
    image (img1 , 0, 0)
    tint (255 , myTintBO )
    image (img2 , 0, 0)
