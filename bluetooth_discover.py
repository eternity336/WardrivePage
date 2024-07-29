from bluetooth import *
import threading

discovered = set()

def lookup_devices():
     while True:
          print("Searching")
          _discovered = discover_devices(duration=30, lookup_names = True)
          for d in _discovered:
               discovered.add(d)

def print_devices():
     for name, addr in discovered:
          print(" %s - %s" % (addr, name))

def get_devices():
     return [[name, addr] for name, addr in discovered]

t1 = threading.Thread(target=lookup_devices)
t1.start()


     
