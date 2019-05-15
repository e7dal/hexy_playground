import click
import time
import hexy
h=hexy.Hexy(34,31)

h.draw(18,2,3)
h.draw(5,14,3)
h.draw(18,26,3)
h.draw(43,26,3)
h.draw(56,14,3)
h.draw(43,2,3)

def hline(x,y,c,s,d):
 for i in range(s,s+1):
  h.line(x,y,c,i,d)
  click.clear()
  print(h.show())
  time.sleep(0.02)

def doloop(a=10):
 for d,c in [("X","_"),
           ("Y","\\"),
           ("Z","/"),
           ("x","_"),
           ("y","\\"), 
           ("z","/")]:
  for i in range(1,a): 
   hline(22+i,6+i,c,i,d)
   click.clear()
   print(h.show())
   time.sleep(0.1)

doloop()
