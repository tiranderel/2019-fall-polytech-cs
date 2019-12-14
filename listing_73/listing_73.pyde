img=None

def setup ():
    global img
    background (100) 
    smooth ()
    size (800 , 800) 
    img = loadImage ("CR.jpg")
    print(img)

def draw ():
    global img
    background (100)
    image (img , mouseX , mouseY )
