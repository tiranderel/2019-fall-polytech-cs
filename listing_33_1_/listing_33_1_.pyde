def setup():
    size(500, 500)
    background(0)
    smooth()
    strokeWeight(1)
    
         
i=0
k=1    
def draw(): 
    global i, k
    stroke(i, 40)
    line(mouseX, mouseY, random(0, 500), 0)
    i=i+k
    if(i==255):
        k=-1
    if(i==0):
        k=1
    
    
    
