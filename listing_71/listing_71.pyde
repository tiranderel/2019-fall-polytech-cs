class MySuperBall:
    x=0
    y=0
    radius=0
    speed=0
    counter=0
    center = 250
    previousBall=None 
    vector = 1

    def render (self):
        noStroke ()
        fill (0 , 150) 
        ellipse (self.x,self.y,self.radius , self.radius )
        stroke (250) 
        strokeWeight (1)
        if self.previousBall!=None:
            print(self.previousBall)
            line (self.x,self.y, self.previousBall.x, self.previousBall.y)
            noStroke ()
        fill (250)
        ellipse (self.x,self.y ,6 ,6)

    def upDate (self):
        self.counter += self.speed * self.vector /300
        self.y = self.center + sin( self.counter ) *30 
        if self.previousBall != None:
            self.center = self.previousBall.y;
        if ( self.counter > TWO_PI ):
            self.vector = self.vector *( -1)

ballArray_one=[]

def setup ():
    size (500 , 500) 
    smooth ()
    myInit ()

def myInit ():
    global ballArray_one
    number = 50
    step = float (width) / float( number )
    ballArray_one = list(range(number))
    for i in range(len(ballArray_one)):
        tmp_obj = MySuperBall ()
        variable = random (0 ,5)
        tmp_obj .x = variable + step *i
        tmp_obj .y = random ( -100 ,100) + 250
        tmp_obj . radius = variable *10 + 5
        tmp_obj . speed = random (0.2 , 10)
        if i > 0:
            tmp_obj . previousBall = ballArray_one [i -1]
        ballArray_one [i] = tmp_obj 
    ballArray_two = ballArray_one 

def draw ():
    global ballArray_one
    background (150) 
    for i,curentBall in enumerate(ballArray_one):
        if i!=0:
            curentBall . upDate ()
        curentBall . render ()

def keyPressed ():
    if key == 'a':
        myInit ()
    if key == 's':
        saveFrame ("myProcessing.png")
