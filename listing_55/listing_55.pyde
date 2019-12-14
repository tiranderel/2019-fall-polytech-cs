class MyLine:
    centerX=0
    centerY=0
    length=0
    angle=0
    weight=0

    def render (self):
        x1 = self.centerX - cos( self.angle )* self.length /2
        y1 = self.centerY + sin( self.angle )* self.length /2
        x2 = self.centerX + cos( self.angle )* self.length /2
        y2 = self.centerY - sin( self.angle )* self.length /2
        stroke (50 , 100) 
        strokeWeight ( self.weight )
        line (x1 , y1 , x2 , y2)
        strokeWeight (5)
        stroke (50) 
        line (x2 , y2 , x2 , y2)
        line (x1 , y1 , x1 , y1)

lineObj=MyLine()
counter=0

def setup ():
    global lineObj
    size (500 , 500) 
    smooth ()
    background (255) 
    #lineObj = MyLine ()
    lineObj . centerX = width /2
    lineObj . centerY = height /2
    lineObj . length = 350
    lineObj . angle = PI /4
    lineObj . weight = 1

def draw ():
    global lineObj, counter
    counter += 0.05
    if counter > TWO_PI:
        counter = 0
    lineObj . centerX = width /2 + sin( counter ) *50
    lineObj . centerY = width /2 + cos( counter ) *50
    lineObj . angle = counter *2
    lineObj . render ()
