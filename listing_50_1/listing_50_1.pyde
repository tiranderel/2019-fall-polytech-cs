def setup():
    size(500, 500)
    smooth()
    background(255)
    strokeWeight(1)
    
counter=0
counter1=0
cx=250
cy=250
cRadius=10

def draw():
    global counter, counter1, cx, cy, cRadius
    stroke(0, 30)
    
    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
    
    x1 = nx - sin(counter)*300
    y1 = ny - cos(counter)*300
    x2 = nx + sin(counter)*300
    y2 = ny + cos(counter)*300
    
    #line(x1, y1, x2, y2)
    bezier(x1, y1, x1-x2, y1-y2, x2-x1, y2-y1, x2, y2)
    bezier(x1, y1, x1+x2, y1+y2, x2+x1, y2+y1, x2, y2)
    
    counter += 0.1
    if counter > 2*PI:
        counter = 0
    zzz=mouseX/ (float (width*2))
    counter1 = counter1 + zzz
    if counter1 > 2*PI:
        counter1 = 0