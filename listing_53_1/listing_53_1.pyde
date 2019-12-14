
class FunnyRect:
    cx =0.
    cy=0.
    fsize=0.
    
    def setCenter (self, x, y):
        self.cx = x
        self.cy = y

    def setSize (self, size):
        self.fsize = size

    def render (self):
        rect (self.cx , self.cy , self.fsize , self.fsize )
        fill (200, 134, 165)
     

funnyRectObj = FunnyRect ()
funnyRectObj1 = FunnyRect ()
counter=0

def setup ():
    global funnyRectObj,funnyRectObj1
    size (600 , 600)
    smooth ()
    noStroke ()
    rectMode ( CENTER )
    funnyRectObj.setSize(50)
    funnyRectObj1.setSize(20)

def draw ():
    global funnyRectObj, funnyRectObj1, counter
    background (255)
    fill (50)
    objX = mouseX + sin( counter ) *150
    objY = mouseY + cos( counter ) *150
    funnyRectObj.setCenter (mouseX , mouseY )
    funnyRectObj.render ()
    funnyRectObj1 . setCenter (objX , objY )
    funnyRectObj1 . render ()
    counter += 0.05
