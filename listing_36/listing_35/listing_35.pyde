def setup():
    size(500, 500)
    smooth()
    background(0)
    strokeWeight(1)
    
i=0
k=1
flug=1
 
   
        
def draw():
    def upDate():
        global i, k
        i=i+k
        if(i==255):
            k=-1
        if(i==0):
            k=1
            
    global i, k, flug
    stroke(i, 20)
    myRandom1 = random(-20, 20)
    myRandom2 = random(-20, 20)    
    myY1=mouseY-myRandom1
    myY2=mouseY+myRandom2
    line(0, myY1, 500, myY2)
    upDate()
   
