import hexy
import click
import time

def do(f,a):
 print(f,a)
 r=f(*a)
 time.sleep(0.01)
 click.clear()
 print(h.show())
 return r

#h=hexy.Hexy(x=27,y=21)
#print(h.show())
h=hexy.Hexy(27,21)
print(h.show())
for i in range(1,183):
 for d in 'XYZxyz':
  do(h.line,(0,0,d,i,d))


#%history?
#%history -f xyz.ipy
