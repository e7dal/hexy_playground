import time
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

