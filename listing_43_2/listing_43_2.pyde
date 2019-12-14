def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)
    
counter=0
nx=0
ny=0
cx=250
cy=250

def draw():
    stroke(200, 20)
    global nx, ny, cx, cy, counter
    for si in range(0,6):
        si=si+1
        for ci in range(0,6):
            ci=ci+1
            nx=ci*71
            ny=si*71
            line(nx, ny, nx, ny)
            x1 = nx - sin(counter)*(50)
            y1 = ny - cos(counter)*(50)
            x2 = ny + sin(counter)*(50)
            y2 = nx + cos(counter)*(50)
            line(x1, y1, x2, y2)
            
            
    counter+=0.1
    if counter>2*PI:
        counter=0
            
