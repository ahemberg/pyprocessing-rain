import random

bgcol = [0,0,0]
drops = []

def setup():  
    size(1024, 768)
    
    for i in range(500):
        drops.append(Drop(width, height))
        
def draw():
    background(bgcol[0],bgcol[1],bgcol[2])
    for drop in drops:
        drop.show()
        drop.fall()
            
class Drop:    
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.dropcol = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        self.x = random.randint(0,self.w)
        self.y = random.randint(-400,0)
        self.yspeed = random.randint(4,10)
        self.dlen = self.jmap(self.yspeed, 4, 10, 1, 10);
        self.xspeed = self.jmap(self.yspeed, 4, 10, -1, 2);

    def fall(self):
        self.y += self.yspeed
        self.x += self.xspeed
        
        if self.y >= self.h:
            self.x = random.randint(0,self.w)
            self.y = random.randint(-400,0)
            
    def show(self):
        stroke(self.dropcol[0],self.dropcol[1],self.dropcol[2])
        line(self.x,self.y,self.x,self.y+self.dlen)
    
    @staticmethod
    def jmap(x, in_min, in_max, out_min, out_max):
        return (x-in_min)*(out_max-out_min)/(in_max-in_min) + out_min
            
             
        
