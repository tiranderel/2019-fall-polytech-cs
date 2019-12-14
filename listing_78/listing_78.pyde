img0 =None
img1 =None

def setup ():
    global img0, img1
    background (100) 
    smooth ()
    noStroke ()
    img0 = loadImage ("CR1.jpg")
    img1 = loadImage ("CR2.jpg")
    size (600 , 800)

def draw ():
    if frameCount == 1:
        image (img1 , 0, 0)
    pointSize = map(mouseX , 0, width , 0, 100) 
    pointAlpha = map(mouseY , 0, height , 0, 255) 

    x = int(random ( img0 . width ))
    y = int(random ( img0 . height ))
    loc = x + y* img0 . width 
    img0 . loadPixels ()
    r = red( img0 . pixels [loc ])
    g = green ( img0 . pixels [ loc ])
    b = blue ( img0 . pixels [loc ])
    
    fill (r,g,b, pointAlpha )
    ellipse (x,y, pointSize , pointSize )

    tint (255 , 2)
    image (img1 , 0, 0)

def  keyPressed ():
    saveFrame (" myProcessing " + frameCount + ".jpg ")
