import click
import time
import hexy
import signal
import sys

def signal_handler(sig, frame):
 print('thanks for watching!Bye:)')
 sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to stop...')
for i in range(3,0,-1):
 print('starting in :%d seconds'%i)
 time.sleep(1.0)

x=44
y=44
a=44
b=23
s=21
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

#h=hexy.Hexy(x,y)
def doloop():
 h=hexy.Hexy(x,y)
 for i in rag(ra,c):
  #h=hexy.Hexy(x,y)
  ai,bi=next(spiral)
  h.draw(a-i-ai,b-i-bi,i)
  print(h.show())
  click.clear()
  time.sleep(0.3)

while True:doloop()
