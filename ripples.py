import click
import time
import hexy
from itertools import cycle
import arrow
import random


PARR=arrow.now()

def p(h,t,s):
 global PARR
 click.clear()
 print(h.show())
 print(s)
 now=arrow.now()
 print('time',PARR,now,now-PARR)
 PARR=now
 print('keeplen',len(KEEP))
 #print('color',hexy.util.colors)
 time.sleep(t)

n=42
H,V=2*n,n
T=0.03
h=hexy.Hexy(H,V)
def roundrange(b,e):
 while True:
  for i in range(b,e):yield i
  for i in range(e,b-1,-1):yield i
  
vc=cycle(roundrange(-V//2,V//2))
hc=cycle(roundrange(-H//2,H//2))
rc=cycle(roundrange(1,V//8))
KEEP=[]
def keep_circle(h,x,y,r,R,c):
 amount=27
 global KEEP
 KEEP.append((x,y,r,R-1,' '))
 if len(KEEP)==amount:
  KEEP.reverse()
  KEEP.pop()  #just remove oldest
  KEEP.reverse()
 ccc=0
 for ca in KEEP:
  #x,y,r,R,c=*ca#
  ccc+=1
  if ccc % 2 == 0:
   h.circle(*ca)
 h.circle(x,y,r,R,'O')
 


def loop():
 c=1
 while 1:
   h=hexy.Hexy(H,V)
   x=next(hc)+H
   y=next(vc)+(V//2)
   r=next(rc)
   c+=1
   #c%=H
   x=c
   y=c
   #x+=random.randrange(-1,1)
   #y+=random.randrange(-1,1)
   #h.circle(x,y,r,r+2,'o')
   keep_circle(h,x,y,r,r+3,'o')
   p(h,T,(x,y,r,r+2))

loop()
