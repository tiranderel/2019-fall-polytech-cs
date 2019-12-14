num = 60;
mx = [0.]*num
my = [0.]*num

def setup ():
    size (640 , 360)
    noStroke ()
    fill (255 , 153) 

def draw ():
    global num, mx, my
    background (51)

    #Cycle through the array , using a different entry on each frame .
    #Using modulo (%) like this is faster than moving all the values over .
    which = frameCount % num
    mx[ which ] = mouseX 
    my[ which ] = mouseY 
    for i in range(num):
        #which +1 is the smallest (the oldest in the array )
        index = ( which +1 + i) % num 
        ellipse (mx[ index ], my[ index ], i, i)
