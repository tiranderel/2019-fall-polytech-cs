class MyEllipse:
    centerX=0.
    centerY=0.
    angle=0.
    size=0.
    weight=0.
    
    def __init__(self, centerX , centerY , angle , size , weight):
        self.centerX = centerX
        self.centerY = centerY
        self.angle = angle
        self.size = size
        self.weight = weight

    def render (self):
        fill (200 , self.size /20) 
        x1 = self.centerX - cos( self.angle )* self.size /2
        y1 = self.centerY + sin( self.angle )* self.size /2
        stroke (250 , 100) 
        strokeWeight ( self.weight )
        ellipse (x1 , y1 , self.size , self.size )

ellipseObj=0


def setup ():
    global ellipseObj
    size (500 , 500) 
    smooth ()
    background (10) 
    ellipseObj = MyEllipse ( width /2, width /2, 0, 150 , 1)

counter=0

def draw ():
    global ellipseObj,counter
    counter += 0.01
    if counter > TWO_PI:
        counter = 0
    ellipseObj . size = sin( counter *4.)* mouseX 
    ellipseObj . render ()
