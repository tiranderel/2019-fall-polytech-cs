counter=0
counter1=0
cx=250
cy=250
nx=0
ny=0
cRadius=20

def setup():
    global nx, ny
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)
    cx=width/2
    cy=height/2
    
def oneLineDraw(ncx, ncy):
    x1 = ncx - sin(counter1)*(100)
    y1 = ncy - cos(counter1)*(100)
    x2 = ncx + sin(counter1)*(100)
    y2 = ncy + cos(counter1)*(100)
    line(x1, y1, x2, y2)
    
def draw():
    global nx, ny, counter, cRadius, counter1
    stroke(200, 25)
    
    nx = sin(counter1)*cRadius + cx
    ny = cos(counter1)*cRadius + cy
    
    x1 = nx - sin(counter)*(60)
    y1 = ny - cos(counter)*(60)
    x2 = nx + sin(counter)*(60)
    y2 = ny + cos(counter)*(60)
    
    oneLineDraw(x2, y2)
    oneLineDraw(x1, y1)
    
    counter += 0.1
    if counter>2*PI:
        counter=0
        
    counter1+=0.01
    cRadius+=counter/20
    
    if counter1>2*PI:
        counter1=0
    
