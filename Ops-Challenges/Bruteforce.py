import random
import time
import os
from tqdm import tqdm
import random
import getpass
import pwnedpasswords
from time import sleep

def loading():
    for index in tqdm(range(100), desc = "Pwning..."):
        time.sleep(0.1)

    pss = pwnedpasswords.__all__
    print("enhance... enhance... enhance...", pss)
    print("SCANNING PASSWORD DIRECTORY")

passwords = {pwnedpasswords.check}

def check_password(passwords):
  print('---checking password---')
  print(passwords)

  for password in passwords:
    print('That is a known password DO NOT use it!!!')
  else:
    print('That is an unknown password')

  sleep(3)

def login():
    usid = input("enter username: ")
    if usid == ("root"):
        pas()
    else:
        end()

def end():
    os.system('cls')
    print("OKIE DOKIE LET ME KNOW WHEN YOU WANT TO bRUTE fORCE AGAIN...")
    exit()


def menu():
    os.system('cls')
    input("enter ip address:")
    os.system('cls')
    print("starting the hunt...")
    time.sleep(2)
    os.system('cls')

    loading()
    time.sleep(2)
    loading()
    time.sleep(2)
    loading()
    time.sleep(2)
    loading()
    time.sleep(2)
    loading()
    time.sleep(2)
    loading()
    time.sleep(2)
    loading()
    time.sleep(2)
    loading()
    time.sleep(2)
    loading()
    print("completed! combine the digits and that's your password...")

check_password()