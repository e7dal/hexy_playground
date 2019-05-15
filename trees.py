import click
import time
import hexy

def p(h,t):
 print(h.show())
 time.sleep(t)


def hline(x,y,c,s,d):
 for i in range(s,s+1):
  h.line(x,y,c,i,d)
  click.clear()
  p(h,0.03)

H,V=70,70
h=hexy.Hexy(H,V)
#x,y=H//2,V//2


def doloop(a,dc,xf,yf):
 for d,c in dc:
  for i in range(1,a): 
   hline(xf(i),yf(i),c,i,d)

X=('X','_')
Y=('Y','\\')
Z=('Z','/')
x=('x','_')
y=('y','\\')
z=('z','/')

dc=[X,Y,Z,x,y,z]
xf=lambda i:i+20
yf=lambda j:j+3
doloop(a=11,dc=dc,xf=xf,yf=yf)


dc=[X,Z,x,Y,y,z]
xf=lambda i:i+40
yf=lambda j:j+23
doloop(a=11,dc=dc,xf=xf,yf=yf)

dc=[X,x,Y,y,Z,z]
xf=lambda i:60
yf=lambda j:j+43
doloop(a=11,dc=dc,xf=xf,yf=yf)

dc=[x,X,y,Y,z,Z]
xf=lambda i:i+60
yf=lambda j:j+3
doloop(a=11,dc=dc,xf=xf,yf=yf)
