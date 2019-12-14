class FunnyEllipse:
    myColor = 200;
    size=0
    x=0
    y=0
    noise=True

    def __init__(self):
        self.size = random (50 , 150)

    def render (self):
        rectMode ( CENTER )
        fill ( self.myColor , 100) 
        noStroke ()
        if self.noise :
            fill ( random (150 ,255) , 150) 
            nx = self.x + noise (self.x) *10
            ny = self.y + noise (self.y) *10
            ellipse (nx , ny , self.size , self.size )
        else:
            ellipse (self.x, self.y, self.size , self.size )

    def isLine (self, box):
        result = False
        if dist (self.x,self.y, box .x, box.y) < 150:
            result = True 
            box . noise = True 
        else:
            box . noise = False 
        self.noise = result 
        return result 

    def drawLine (self, box):
        stroke (255) ;
        strokeWeight (1);
        line (self.x, self.y, box .x, box.y);
        noStroke ();
        fill (10) ;
        ellipseMode ( CENTER );
        ellipse (self.x, self.y, 10, 10);
        ellipse ( box.x, box.y, 10, 10);

obj_1=FunnyEllipse()
obj_2=FunnyEllipse()
counter = 0

def setup ():
    size (500 , 500) 

def draw ():
    global obj_1, obj_2, counter
    background (10)
    obj_1 .x = map(sin( counter ) , -1,1,100, width -100)
    obj_2 .x = map(cos( counter ) , -1,1,100, width -100)
    obj_1 .y = map(cos( counter + 0.1) ,-1,1 ,100 , width -100)
    obj_2 .y = map(sin( counter - 0.1) ,-1,1 ,100 , width -100)
    obj_1 . render ()
    obj_2 . render ()
    if obj_1 . isLine ( obj_2 ):
        obj_1 . drawLine ( obj_2 )
    counter += 0.01
