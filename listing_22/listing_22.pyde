def setup():
    size(590, 750)
    smooth()
    background(255)
    noStroke()
    noLoop()
    

def draw():
    i= range(0, 10)
    for i in range (0, 10):
        i = i+1
        fill (i*20)
        rect(i*40+50, 220, 35, 35)
    for i in range (0, 10):
        i = i+1
        fill (200-i*20)
        rect(i*40+50, 260, 35, 35)
    for i in range (0, 10):
        i = i+1
        fill (i*20)
        rect(i*40+50, 300, 35, 35)
    for i in range (0, 10):
        i = i+1
        fill (200 - i*20)
        rect(i*40+50, 340, 35, 35)
    for i in range (0, 10):
        i = i+1
        fill (i*20)
        rect(i*40+50, 380, 35, 35)
    for i in range (0, 10):
        i = i+1
        fill (200-i*20)
        rect(i*40+50, 420, 35, 35)
    for i in range (0, 10):
        i = i+1
        fill (i*20)
        rect(i*40+50, 460, 35, 35)
    for i in range (0, 10):
        i = i+1
        fill (200-i*20)
        rect(i*40+50, 500, 35, 35)
    for i in range (0, 10):
        i = i+1
        fill (i*20)
        rect(i*40+50, 540, 35, 35)
    for i in range (0, 10):
        i = i+1
        fill (200-i*20)
        rect(i*40+50, 580, 35, 35)
