img0 =None
img1 =None
img2 =None
img3 =None
def setup ():
    global img0, img1, img2, img3
    background (100) 
    smooth ()
    img0 = loadImage ("CR0.jpg")
    img1 = loadImage ("CR1.jpg")
    img2 = loadImage ("CR2.jpg")
    img3 = loadImage ("CR3.jpg")
    size (720 , 500) 

def draw ():
    background (100) 
    image (img0 , 0, 0)
    image (img1 , mouseX * 0.65, 200) 
    image (img2 , 450, 320)
    image (img3 , width - mouseX * 0.6-300 , 100)
