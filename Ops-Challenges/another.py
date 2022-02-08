#!/usr/env python

# Description: this file does something
# Author: Aaron W Haws
# Last updated 11/30/2021

import socket
import sys
import time

# Function definition does not execute until function invocation

def simple_math(nums):
    total = 0
    for item in nums[1:]:
         total += int(item) | 0
         time.sleep(.25)
         print("  [~] running total: ",total)
         print("what is the sum of your numbers", total)

def get_host_ip():
         host = socket.getaddrinfo(socket.gethostname(), 1)
         print (host)

def main(args):
     # Do some work
     get_host_ip()
     host = socket.getaddrinfo(socket.gethostname(), 1)
     print (host)

# Function execution
if __name__ == '__main__':
     main(sys.argv)


# another test