#! python3

# uptime monitor
import os
from pdb import main
from select import error
from pythonping import ping

class machine:
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

machines = [
    machine("google", "8.8.8.8"),
    machine("cloudflare", "1.1.1.1"),
    machine("codeworks", "104.21.13.205")
]

def ping_machines():
    for machine in machines:
      try:
        status = str(ping(machine.ip, size=1500))
        print("what is the status?", status)
        if status.startswith("reply"):
            print(machine.name, "is up")
        else:
            print(machine.name, "is down")   
      except ValueError:
        print(f"{machine.name} - {machine.ip} is not a valid target")

def add_new_machine():
    name = input("what is the name of the machine? ")
    ip = input("what is the ip of the machine? ")
    machines.append(machine(name,ip))

def print_menu():
    print("""
    What would you like to do?

    1 - add new machine
    2 - ping machine
    3 - list machine
    4 - quit
    

    """)
        userchoice = input("what would you like to do? ")

        if options[userchoice]:
           options[userchoice]()
        else:
            print(f"sorry but {userchoice} is not valid")
            sleep(1)



options = {
"1": add_new_machine
"2": ping_machines
"3": list_machines
"4": quit
}

def main():
    print_menu()


def list_machines():


def quit_program():
    print("okay bye.")
    exit(0)

main()





