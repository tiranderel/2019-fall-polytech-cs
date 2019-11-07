def setup():
    size(600, 500)
    smooth()
    background(255)
    strokeWeight(30)
    noLoop()
    
def draw():
    stroke(20, 100)
    i = range(1, 8)
    for  i  in range(1, 5):
        line(i*2*50, 200, 150 + (2*i-1)*50, 300)
        line(i*2*50 + 100, 200, 50 + (2*i-1)*50, 300)
