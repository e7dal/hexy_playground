import click
import time
import hexy
import stop_and_thanks
x=44
y=44
a=44
b=23
s=21
c=1
def r():
 a=[]
 for i in range(1,s):a.append(i)
 for i in range(s,0,-1):a.append(i)
 return a

ra=r()
def rag(a,d=3):
 for i in a:
  if i%d==0:yield i

def doloop():
 global c
 if c%3==0:c=1
 c+=1
 h=hexy.Hexy(x,y)
 for i in rag(ra,c):
  #h=hexy.Hexy(x,y)
  h.draw(a-i,b-i,i)
  print(h.show())
  click.clear()
  time.sleep(0.3)

while True:doloop()
