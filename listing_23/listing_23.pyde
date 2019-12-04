def setup():
    size(500, 500)
    smooth()
    noLoop()
    noStroke()
    ellipseMode(CENTER)   
    
    
def draw():
    background(255)
    border = 40
    nw = width - 2*border
    nh = height - 2*border
    number = 5
    nWstep = nw/number
    nHstep = nh/number
    for i in range(0, number):
        for j in range(0, number):
            x = border + j*nWstep + nWstep/2
            y = border + i*nHstep + nHstep/2
            size = (j+i)*max([nWstep, nHstep])/10
            sizemax =(number*2-2)*max([nWstep, nHstep])/10
            nColor=(sizemax-size)*5
            fill(0, 0, nColor)
            ellipse(x, y, 5+sizemax-size, 5+sizemax-size)
            fill(250)
            ellipse(x, y, 3, 3)
            
            
