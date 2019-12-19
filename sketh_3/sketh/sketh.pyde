add_library('sound')
from processing import sound
s = sound.Sound(this)
 

device = None
fft = None
r_width=0
pointSize=6

scale = 0.5
bands = 64
sum = [0.0] * bands
smooth_factor = 0.2
r1=1
r2=1
r3=1
r4=1

def setup():
    fullScreen()
    background(0)
    global device, img
    img = loadImage("logo3.jpg")
    #noLoop()
    
    global s
    sin = sound.SoundFile(this, 'mcr.wav')
    sin.play()
     
    global fft
    fft = FFT(this, bands)
    fft.input(sin)
    
def draw():
    global s, img, pointSize
    amplitude = map(mouseY, 0, height, 0.4, 0.0)
    s.volume(0.7)
    
    x=int(random(img.width))
    y=int(random(img.height))
    #print(x,y)
    
    loc= int(x+y*img.width)
    
    loadPixels()
    r=red(img.pixels[loc])  
    b=blue(img.pixels[loc])
    g=green(img.pixels[loc])  
    
    fill(r, g, b, 255)
    noStroke()
    c1=(width-img.width)/2
    circle(c1+x, y, pointSize) 
    #print(x,y)
    #image(img, 0, 0)
    #noStroke()
    
    global r1, r2, r3, r4
    c2=width/6
    c3=(height-img.height)/2
    c4=1.2*c3+img.height
    c5=min(c2,c3)
    
    fft.analyze()
    #print (fft.spectrum[:12])
    fill(0,0,0,255)
    noStroke()
    circle(c2, c4, r1+1) 
    fill(300*fft.spectrum[1], 300*fft.spectrum[2], 300*fft.spectrum[3], 255)
    r1=0.53*c5*fft.spectrum[0]
    noStroke()
    circle(c2, c4, r1) 

    fill(0,0,0,255)
    noStroke()
    circle(c2*3, c4, r2+1) 
    fill(400*fft.spectrum[5], 400*fft.spectrum[6], 400*fft.spectrum[7], 255)
    r2=2.10*c5*fft.spectrum[4]
    noStroke()
    circle(c2*3, c4, r2) 

    fill(0,0,0,255)
    noStroke()
    circle(c2*5, c4, r3+1) 
    fill(400*fft.spectrum[9], 400*fft.spectrum[10], 400*fft.spectrum[11], 255)
    r3=3.25*c5*fft.spectrum[8]
    noStroke()
    circle(c2*5, c4, r3) 

    #for i, v in enumerate(sum):
    #    sum[i] += (fft.spectrum[i] - v) * smooth_factor
    #    print(sum[i])
    #    fill(255, 0, 150)
    #    circle(width/2, height/2, -sum[i] * 400 * scale)
   

 
                            
    
