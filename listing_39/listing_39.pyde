def setup():
    size(500, 500)
    smooth()
    background(50)
    strokeWeight(5)
    
cx=250
cy=250
cRadius=200

def draw():
    stroke(250)
    global cx, cy, cRadius
    i=0
    while i<2*PI:
        i=i+2*PI/12
        x1= cos(i)*cRadius+cx
        y1= sin(i)*cRadius+cy
        line(x1, y1, x1, y1)
    line(cx, cy, cx, cy)
    
        
