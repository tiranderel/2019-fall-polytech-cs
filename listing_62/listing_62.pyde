xCoordinate = list(range(10))

def setup ():
    global xCoordinate
    size (500 , 500)
    smooth ()
    noStroke ()
    for i in range(len(xCoordinate)):
        xCoordinate [i] = 35*i + 90

def draw ():
    background (50) 
    for i in range(len(xCoordinate)):
        fill (200 , 40)
        ellipse ( xCoordinate [i], 250 , 15*i, 15* i)
        fill (0)
        ellipse ( xCoordinate [i], 250 , 3, 3)

def keyPressed ():
    if key == 's':
        saveFrame ("myProcessing .png")
