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
  p(h,0.01)

def doloop(a=17):
 for d,c in [('X','_'),
             ('Y','\\'),
             ('Z','/'),
             ('x','_'),
             ('y','\\'), 
             ('z','/') ]:
  for i in range(1,a): 
   hline(25+i,7+i,c,i,d)

H,V=70,70
h=hexy.Hexy(H,V)
#x,y=H//2,V//2
x=100
y=55

for s in range(5):
 #s=7
 h.draw(x-18,y-2, s)
 h.draw(x-5, y-14,s)
 h.draw(x-18,y-26,s)
 h.draw(x-43,y-26,s)
 h.draw(x-56,y-14,s)
 h.draw(x-43,y-2, s)
 p(h,0.01)
doloop()
