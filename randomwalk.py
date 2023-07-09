import math,random,pylab

class location(object):
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
    def move(self,xc,yc):
        return location(self.x+float(xc),self.y+float(yc))
    def getcoords(self):
        return self.x,self.y
    def getdist(self,other):
        ox,oy=other.getcoords()
        xdist=self.x-ox
        ydist=self.y-oy
        return math.sqrt(xdist**2 + ydist**2)
    
    
class compasspt(object):
    possibles=('n','s','e','w')
    def __init__(self,pt):
        if pt in self.possibles:self.pt=pt
        else:raise ValueError('in compasspt.__init')
    def move(self,dist):
        if self.pt =='n':return (0,dist)
        elif self.pt == 's':return (0,-dist)
        elif  self.pt == 'e' :return (dist,0)
        elif self.pt =='w' :return (-dist,0)
        else:raise ValueError('in compasspt.move')
        
class field(object):
    def __init__(self,drunk,loc):
        self.drunk=drunk
        self.loc=loc
    def move(self,cp,dist):
        oldloc=self.loc
        xc,yc=cp.move(dist)
        self.loc=oldloc.move(xc,yc)
    def getloc(self):ac
        return self.loc
    def getdrunk(self):
        return self.drunk
    

class drunk(object):
    def __init__(self,name):
        self.name=name
    def move(self,field,time=1):
        if field.getdrunk()!=self:
            raise ValueError('drunk.move called with drunk not in  the field')
        for i in range(time):
            pt=compasspt(random.choice(compasspt.possibles))
            field.move(pt,1)
            
            
      



      
def performtrial(time,f):
    start=f.getloc()
    distances=[0.0]
    for t in range(1,time+1):
        f.getdrunk().move(f)
        newloc=f.getloc()
        distance=newloc.getdist(start)
        distances.append(distance)
    return distances


def firsttest():
    drunk1=drunk('ravan')
    for i in range(5):
         f=field(drunk1,location(0,0))
         distances=performtrial(1,f)
         pylab.plot(distances)
    pylab.show()
    pylab.xlabel('time')
    pylab.ylabel('distance from  origin')
    pylab.title('average distance vs time')
   




#assert False
def performsim(time,numtrials):
    distlists=[]
    for trial in range(numtrials):
        d=drunk('drunk' +str(trial))
        f=field(d,location(0,0))
        distances=performtrial(time, f)
        distlists.append(distances)
    return distlists
        
        

def ansquest(maxtime,numtrials):
    means=[]
    distlists=performsim(maxtime, numtrials)
    for t in range(maxtime +1):
        tot=0.0
        for distl in distlists:
            tot+=distl[t]
       # print(tot)
        means.append(tot/len(distlists))
      #  print(means)
    pylab.figure()
    pylab.plot(means)
    pylab.ylabel('distance')
    pylab.xlabel('time')
    pylab.title('average distance vs time ('+str(len(distlists))+'trail)')
    
ansquest(500,100)
pylab.show()