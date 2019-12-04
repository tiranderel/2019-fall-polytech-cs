def setup():
    background(255)
    size(500, 500)
    smooth()
    
l1x1 = 0
l1y1 = 0
l1x2 = 500
l1y2 = 500
flug = 1
cl1=200
cl2=20
cl3=20



def draw():
    global l1x1, l1y1, l1x2, l1y2, flug, cl1, cl2, cl3
    background (255)
    strokeWeight(50)
    stroke(cl1, cl2, cl3, 20)
    line(l1x1, l1y1, l1x2, l1y2)
    i=1
    while i<20:
        i=i+1
        k= i*50
        stroke(cl1, cl2, cl3+i*10, 20+i*10)
        line(l1x1 + k, l1y1, l1x2, l1y2 - k)
        line(l1x1, l1y1 + k, l1x2 - k, l1y2)
        
    l1x1 = l1x1 + flug
    l1y1 = l1y1 + flug
    l1x2 = l1x2 - flug
    l1y2 = l1y2 - flug
    if l1x1==l1x2:
        if flug ==1:
            cl1=20
            cl2=200
            cl3=20
        else:
            cl1=200
            cl2=20
            cl3=20
    if (l1y2<0 or l1y2>500):
        flug = (-1)*flug
        
