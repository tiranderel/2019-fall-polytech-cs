i=0
k=1
class MyLine:
    centerX=0
    centerY=0
    length=0
    angle=0
    weight=0
    def upDate():
        global i, k
        i=i+k
        if(i==255):
            k=-1
        if(i==0):
            k=1

    def render (self):
        global i, k
        x1 = self.centerX - cos( self.angle )* self.length /2
        y1 = self.centerY + sin( self.angle )* self.length /2
        x2 = self.centerX + cos( self.angle )* self.length /2
        y2 = self.centerY - sin( self.angle )* self.length /2
        stroke (50) 
        strokeWeight ( self.weight )
        line (x1 , y1 , x2 , y2)
        strokeWeight (5)
        stroke (145-i, 89) 
        line (x2, y2, x2, y2)
        stroke (145, 111-i, 89)
        line (x1 , y1 , x1 , y1)

lineObj=MyLine()
counter=0
radius=0

def setup ():
    global lineObj, radius
    size (500 , 500) 
    smooth ()
    background (0) 
    #lineObj = MyLine ()
    lineObj . centerX = width /2
    lineObj . centerY = height /2
    lineObj . length = 350
    lineObj . angle = PI /4
    lineObj . weight = 1
    radius=50

def draw ():
    global lineObj, counter, radius
    counter += 0.05
    if counter > TWO_PI:
        counter = 0
        radius+=50
    lineObj . centerX = width /2 + sin( counter ) *radius
    lineObj . centerY = width /2 + cos( counter ) *radius
    lineObj . angle = counter *2
    lineObj . render ()
