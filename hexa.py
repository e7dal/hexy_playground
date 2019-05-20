import time
import click

import hexy                                                                                                                               

dp='XYZxyz' #directions path
def dpm(s): # '' multiply
 r=''
 s-=1
 for c in dp:
  r+=s*c
 #print(s,r)
 #time.sleep(1)
 return r

for i in range(2,111,3):
 h=hexy.Hexy(42,27)                                                                                                                        
 hexy.grid.grid_add_hexagon(h.grid,12,6,i,dpm(i))
 click.clear()
 print(h.show())
 time.sleep(0.3)
 
