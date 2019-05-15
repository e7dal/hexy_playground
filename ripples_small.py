import click
import time
import hexy
from itertools import cycle

def p(h,t,s):
 click.clear()
 print(h.show())
 print(s)
 time.sleep(t)

n=81
H,V=n,n
T=0.03
h=hexy.Hexy(H,V)
def roundrange(b,e):
 while True:
  for i in range(b,e):yield i
  for i in range(e,b-1,-1):yield i

  
vc=cycle(roundrange(-V//2,V//2))
hc=cycle(roundrange(-H//2,H//2))
rc=cycle(roundrange(1,4*V))

def loop():
 c=1
 while 1:
   h=hexy.Hexy(H,V)
   x=next(hc)+H
   y=next(vc)+(V//2)
   r=next(rc)
   c+=3
   c%=H
   x+=c
   y+=c
   h.circle(x,y,r,r+2,'o')
   p(h,T,(x,y,r,r+2))

loop()
