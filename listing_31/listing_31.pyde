def setup():
    size(300, 300)
    smooth()
    strokeWeight(30)
    background(0)
    
def draw():
    stroke(200, 20)
    line(mouseX-50,mouseY-50, 100+mouseX-50, 100+mouseY-50)
    line(100+mouseX-50,mouseY-50, mouseX-50, 100+mouseY-50)
    
     
