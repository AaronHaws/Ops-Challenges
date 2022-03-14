import datetime
import os
import time
from time import sleep 
# import smtplib, ssl

host = input('What is the IP? ')
delay = input('How often do you want to check the host (seconds)? ')
emailTo = input('in the event the server goes down what email would you like to be notified?')
password = input('please supply your email password')
port = 587
context = ssl.create_default_context()


def send_email(subject, message):    
    with smtplib.SMTP('smtp-mail.outlook.com', port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(emailTo, password)
        server.sendmail(emailTo, emailTo, f"""From: {emailTo}
Subject: {subject}

{message}
""")
    server.close()
    print("Email sent")
    

def send_ping_request():
    currentTime = datetime.datetime.now()
    response = os.system('ping ' + host)
    status = f'{currentTime} - {host}\n'
    file = open('uptime.log', 'a')
    if response == 0:
        file.write(f'UP: {status}')
    else:
        file.write(f'DOWN:  {status}')
        send_email('[Server is down]', status)
        exit(1)
    sleep(int(delay))
    send_ping_request()






send_ping_request()