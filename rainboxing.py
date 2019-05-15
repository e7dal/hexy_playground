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

def doloop(a=1):
    for i in range(a): 
        hline(20,6,"/",8,"Z")
        hline(11,18,"\\",8,"Y")
        hline(25,28,"_",8,"X")
        hline(49,27,"/",8,"z")
        hline(58,15,"\\",8,"y")
        hline(44,4,"_",8,"x")
        click.clear()
        print(h.show())
        time.sleep(0.1)

def doloopi1(a=1):
    for i in range(a): 
        hline(22,6,"/",9,"Z")
        hline(12,17,"\\",9,"Y")
        hline(25,27,"_",9,"X")
        hline(47,27,"/",9,"z")
        hline(57,16,"\\",9,"y")
        hline(45,5,"_",9,"x")
        click.clear()
        print(h.show())
        time.sleep(0.1)
def doloopi2(a=10):
    for i in range(a): 
        hline(24,6,"/",10,"Z")
        hline(13,16,"\\",10,"Y")
        hline(25,26,"_",10,"X")
        hline(45,27,"/",10,"z")
        hline(56,17,"\\",10,"y")
        hline(46,6,"_",10,"x")
        click.clear()
        print(h.show())
        time.sleep(0.1)
doloop()
doloopi1()
doloopi2()
