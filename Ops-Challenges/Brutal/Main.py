import os

import password_checker
#import ssh_attacker

options = {
  '1': password_checker.start,
#  '2': ssh_attacker.start,
  'q': quit,
  'Q': quit
}

1
def main():
  print("""
Please Select an option
1 - Check Password
2 - SSH Brute Login
Q - Quit
""")
  choice = input("> ")
  if choice in options:
    options[choice]()
  else:
    print("Invalid Option")
  os.system('cls')
  main()

def quit():
  print('OKAY BYE!!!')
  exit(0)

main()