a = list(map(lambda x: [0,0], range(500)))

def setup ():
    global a
    size (500 , 500) 
    for i in range(len(a)):
        for j in range(len(a[i])):
            a[i][j] = random (10 ,490)

def draw ():
    global a
    smooth ()
    noStroke ()
    background (0) 
    for i in range(len(a)):
        eDist = dist (mouseX , mouseY , a[i][0] , a[i ][1]) 
        eSize = map(eDist , 0, 200 , 5, 100) 
        eColor = map(eDist , 0, 200 , 50, 255) 
        fill ( eColor , 200) 

        cx = noise ( mouseX )*10 + a[i ][0]
        cy = noise ( mouseY )*10 + a[i ][1]
        #print(a[i ][1])
        ellipse (cx , cy , eSize , eSize )
