class MyPoint:
    x=0.
    y=0.

    def __init__(self, newX , newY ):
        self.x = newX 
        self.y = newY

    def isDistanceLessThen (self, dist1 , point ):
        result = False
        currentDist = dist ( point .x, point .y, self.x, self.y)
        if currentDist < dist1:
            result = True 
        return result

myPoints = []
currentPoint = None
currentDist = 10.0

def setup ():
    global myPoints, currentPoint, currentDist
    print (dist(0,0,0,0))
    size (500 , 500)
    smooth ()
    background (255)
    strokeWeight (1)

def draw ():
    global myPoints, currentPoint, currentDist
    stroke (0, 20)
    currentPoint = MyPoint (mouseX , mouseY )
    myPoints .append ( currentPoint )
    upDate ()

def upDate ():
    global myPoints, currentPoint, currentDist
    for pointFromArray in myPoints:
        if pointFromArray . isDistanceLessThen ( currentDist ,currentPoint ):
            line ( pointFromArray .x, pointFromArray .y, currentPoint.x, currentPoint .y)

def keyPressed ():
    global myPoints, currentPoint, currentDist
    if key == 's': 
        saveFrame ("myProcessing.png");
        for i in range(10):
            if key == Integer.toString(i).charAt(0):
                currentDist = 10*i
