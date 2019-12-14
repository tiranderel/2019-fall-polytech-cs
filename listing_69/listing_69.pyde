import math

class MySuperBall:
    x=0
    y=0
    radius=0
    speed=0
    previousBall=None 
    vector = 1

    def render (self):
        noStroke ()
        fill (200 , 100) 
        ellipse (self.x,self.y,self.radius , self.radius )
        stroke (10) 
        strokeWeight (2)
        if self.previousBall!=None:
            print(self.previousBall)
            line (self.x,self.y, self.previousBall.x, self.previousBall.y)
            noStroke ()
        fill (0)
        ellipse (self.x,self.y ,6 ,6)

    def upDate (self):
        self.y = self.y + self.speed * self.vector 
        if (self.y > 500) | (self.y < 0):
            self.vector = self.vector *( -1)

step = 30;
ballArray_one=[]
ballArray_two=[]

def setup ():
    size (500 , 500) 
    smooth ()
    myInit ()

def myInit ():
    global ballArray_one, ballArray_two, step
    ballArray_one = list(range(15))
    for i in range(len(ballArray_one)):
        tmp_obj = MySuperBall ()
        variable = random (5 ,30)
        tmp_obj .x = variable + step *i + 20
        tmp_obj .y = random ( -100 ,100) + 100
        tmp_obj . radius = variable *2 + 10
        tmp_obj . speed = random (0.2 , 10)
        if i > 0:
            tmp_obj . previousBall = ballArray_one [i -1]
        ballArray_one [i] = tmp_obj 
    ballArray_two = ballArray_one 


def draw ():
    global ballArray_one
    background (50) 
    for curentBall in ballArray_one:
        curentBall . upDate ()
        curentBall . render ()

def keyPressed ():
    if key == 'a':
        myInit ()
    if key == 'q':
        ballArray_two [0]. radius = 300
