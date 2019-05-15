import hexy
import click
import time

h=hexy.Hexy(42,42)
print(h.show())
#%history -f xyz.py
for d in 'XYZxyz':
    click.clear()
    time.sleep(0.5)
    h.line(0,0,d,42,d)
    print(h.show())
