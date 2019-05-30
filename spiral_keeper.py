#extreme lazy programming ahead, start yaw
#ning:) this is just little script that ju
#st needs to be able to run single or batc
#h data

import sys

from time      import sleep   as         S
from hexy      import Hexy    as         H
from itertools import cycle   as         I 
from random    import randint as         T

#import click #just used click.clear()
#just copied the bything parth here:)

def myclear():
 '''Clears the terminal screen.  This will have the effect of clearingx'''
 sys.stdout.write('\033[2J\033[1;1H')
C=myclear

x=127
y=74

a=x
b=y//2
s=69#x//4
c=3

def r():
 a=[]
 for i in range(s,0,-1):a.append(i)
 #for i in range(1,s):a.append(i)
 return a

ra=r()
def rag(a,d=3):
 for i in a:
  if i%d==0:yield i

#/>\ #  612
#\</ #  543
R= ( 1, 0) #1
yD=( 1, 1) #2
zD=(-1, 1) #3
L= (-1, 0) #4
zU=(-1,-1) #5
yU=( 1,-1) #6

def sp():
 while True:
  yield R  #>#1
  yield yD #\#2
  yield zD #/#3
  yield L  #<#4
  yield zU #\#5
  yield yU #/#6

spiral=sp()

#h=hexy.Hexy(x,y) # if you want a global, remembering hexy object.

def doloop(no=1,f=37,hc=False):
 if not hc:h=H(x,y)
 fc=0
 rand=False    #this line should be implicit
               #next line defines previous line..
 if no==2:rand=True
 for i in rag(ra,c):
  fc+=1
  if fc>f:break
  ai=bi=1
  if hc:h=H(x,y)
  if no:ai,bi=next(spiral)
  h.draw(a-i-ai,b-i-bi,i)
  print(h.show())
  #click.clear()
  #myclear()
  C()
  #time.sleep(0.3)
  S(0.3)

#h=H(x,y)
#while True:doloop()
doloop(0,111,0)
doloop(1,112,0)
doloop(1,114,0) 
doloop(1,114,1) 
doloop(2,114,0) #random values, loops forever, depending on your speed, you might see white noise...

#reverse?
#to be run as fish shell command:
#(hexy_playground) rdl@rdl1810 ~/e/hexy_playground> for i in (seq 1 1111);time python spiral_fuller.py ;sleep 3;echo "starting: $1 on " (date) "bye!" ;end
###for i in (seq 1 111);time python spiral_fuller.py;sleep 0.1;end
##for i in (seq 1 111);time python spiral_fuller.py ;echo "starting: $1 on " (date) "bye!" ;sleep 0.1;end
##for i in (seq 1 1111);time python spiral_fuller.py ;sleep 3;echo "starting: $1 on " (date) "bye!" ;end
#to run this do:
##ag --no-numbers '^###' spiral_fuller.py |sed 's/^###//'|fish

