numberOfellipse = 10
step = 50
a = [[50 ,133 ,40],[132 ,87 ,90],[12 ,287 ,10],[300 ,407 ,30],[232 ,187 ,190],[448 ,300 ,79],[460 ,450 ,32]]

def setup ():
    size (500 , 500) 
    smooth ()
    noStroke ()

counter = 0;

def draw ():
    global numberOfellipse, step, a, counter
    background (127) 
    for i in range(len(a)):
        angle = counter /( float ) (1+i)
        myC = map(sin( angle ), -1, 1, 0, 255) 
        fill ( myC);
        ellipse (a[i][0] , a[i][1] , a[i][2] , a[i ][2]) 
        counter +=0.01
