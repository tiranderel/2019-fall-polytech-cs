img1 =None
img2 =None
img3 =None
isAnimate = True
currentFrame = 1

def setup ():
    global img1, img2, img3, isAnimate, currentFrame
    background (100) 
    smooth ()
    size (800 , 800)
    frameRate (12)
    img1 = loadImage ("CR1.jpg")
    img2 = loadImage ("CR2.jpg")
    img3 = loadImage ("CR3.jpg")

def draw ():
    global img1, img2, img3, isAnimate, currentFrame
    background (100)
    if isAnimate: 
        if  currentFrame==1:
            image (img1 , mouseX , mouseY )
        elif currentFrame==2:
            image (img2 , mouseX , mouseY )
        elif currentFrame==3:
            image (img3 , mouseX , mouseY )
        currentFrame +=1
        if  currentFrame > 3:
            currentFrame = 1
    else:
        image (img1 , mouseX , mouseY )

def keyPressed ():
    global isAnimate
    if isAnimate:
        isAnimate = False
    else:
        isAnimate=True
