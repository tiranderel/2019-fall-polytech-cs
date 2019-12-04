def setup():
    size(500, 500)
    background(0)
    smooth()
    strokeWeight(1)
    
    
def draw(): 
    stroke(255, 255, 255)
    x= mouseX
    y= mouseY
    if (x<y) & (500-x<y):
        line(x, y, random(0, 500), 0)
    elif (x<500-y) & (500-x<500-y):
        line(x, y, random(0, 500), 500)
    elif (y<500-x) & (500-y<500-x):
        line(x, y, 500, random(0, 500))
    else:
        line(x, y, 0, random(0, 500))
 
    
    
