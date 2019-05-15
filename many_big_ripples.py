import click
import time
import hexy
from itertools import cycle

n=131
H,V=n,n
T=0.3
S=42
keep=[]
mk=5
assert mk>0

def p(h,ca,m,s=0):
 if not s:click.clear()
 h.circle(*ca)
 if s:
  print(h.show())
  print(m)
  time.sleep(T)

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
  x=next(hc)+H
  y=next(vc)+(V//2)
  r=S+next(rc)
  c+=3
  c%=H
  x+=c
  y+=c
  #h.circle(x,y,r,r+2,'o') move to p
  m='c: %d, x:%d,y:%d, r:%d, R:%d, len(keep):%d'%(c,x,y,r,r+2,len(keep))
  ca=(x,y,r,r+2,'o')
  #p(h,ca,T,m)
  keep.append((ca,m))
  while len(keep)>mk:del(keep[0])
  h=hexy.Hexy(H,V)
  for ca,m in keep:
   p(h,ca,m,0)
  p(h,ca,m,1)
  #ci()
loop()
