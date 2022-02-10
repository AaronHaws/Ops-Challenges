#!/usr/bin/env python3

import os

def files():{
    for each file in files()
        echo "please enter your" file name:
        read file name
        echo $file name
    else print "no file"
}

print files()

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
