def setup():
    size(500, 500)
    smooth()
    background(255)
    colorMode(RGB)
    noStroke()
    
flug = 0
def draw():
    global flug
    for i in range(1, 10):
        for j in range(1, 10):
            if flug==0:
                fill(0, 0, random(10, 250))
            elif flug==1:
                fill(0, random(0, 255), 0)
            elif flug==2:
                fill(random(0,255), 0, 0)
            else:
                t=random(0, 255)
                fill(t, t, 0)
            rect(j*40+50, i*40+50, 35, 35)
            rect((10-j)*40+10, i*40+50, 35, 35)
              
              
def mouseClicked():
    global flug
    flug=(flug+1)%4
