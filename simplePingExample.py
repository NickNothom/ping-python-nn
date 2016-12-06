#!/usr/bin/python -u
#simplePingExample.py
from Ping import Ping1D
import sys
import getopt

device = ''
instructions = "Usage: python simplePingExample.py -d <device_name>"

##Parse Command line options
############################
try:
    options, remainder = getopt.getopt(sys.argv[1:],"hd:",["help", "device="])
except:
    print(instructions)
    exit(1)

for opt, arg in options:
    if opt in ('-h', '--help'):
        print(instructions)
        exit(1)
    elif opt in ('-d', '--device'):
        if (arg != ''):
            device = arg
    else:
        print(instructions)
        exit(1)

#Make a new Ping
myPing = Ping1D(device)

print("Starting Ping..")
print("Press CTRL+Z to exit")
print("------------------------------------")

#Read and print depth measurements with confidence
while True:
    myPing.updateSonar()
    print("Current Depth: " + str(myPing.getDepth()) + " | Confidence: " + str(myPing.getConfidence()))
