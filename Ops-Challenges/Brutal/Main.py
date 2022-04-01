import os
import password_checker
import SSH_attacker
from colors import colors
import zip_brute

options = {
'1': password_checker.start,
'2': SSH_attacker.start,
'3': zip_brute.zip_brute,
'q': quit,
'Q': quit,
}

def main():
  print(f"""
Please Select an option
{colors.GREEN}1 - Check Password
{colors.GREEN}2 - SSH Brute Login
{colors.GREEN}3 - Zip Brute
{colors.FAIL}Q - Quit{colors.ENDC}
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