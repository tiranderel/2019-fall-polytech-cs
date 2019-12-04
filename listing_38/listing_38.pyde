def setup():
    size(500, 500)
    smooth()
    background(150)
    strokeWeight(1)
flug=1
def draw():
    global flug
    stroke(flug, 20)
    myY2 = random(-50,50)
    myX2 = random(-50,50)
    ellipse(mouseX, mouseY, myY2, myX2)
    fill(255, 255, 255, random(0, 255))
