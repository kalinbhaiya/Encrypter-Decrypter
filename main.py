import pyAesCrypt
import sys
from email.message import EmailMessage
import smtplib
import os
import socket
import colorama
from colorama import Fore, Style
import platform
import time

colorama.init(autoreset=True)
def Print(sentence,color):
    return (color+sentence)

def Banner():
    print(Fore.RED+Style.BRIGHT+"""
#########  ##        #      ############  ########       ##########       #############
#          # #       #     #              #       #      #               #
#          #  #      #    #               #        #     #              # 
#          #   #     #   #                #         #    #             #
#########  #    #    #  #                 #          #   ##########   # 
#          #     #   #   #                #           #  #             #
#          #      #  #    #               #           #  #              #
#          #       # #     #              #          #   #               #
#########  #        ##      ############  ##########     ##########       ##############
    
    """)
    print(Print('Created By : ',Fore.LIGHTYELLOW_EX),end='')
    print(Print('Muhammad Muzammil Alam',Fore.RED))
    print(Print('Github : ',Fore.LIGHTYELLOW_EX),end='')
    print(Print('https://github.com/kalinbhaiya',Fore.RED),end='\n\n')
Banner()

choice1 = print(Print('1 To Encrypt 2 To Decrypt : ',Fore.GREEN),end='')
choice = input()
if choice=='1':
    filename = print(Print('Enter The Name Of The File You Want To Encrypt : ',Fore.GREEN),end='')
    filename1 = input()
    encrypted = print(Print('Enter The New Name Of The Encrypted File (with .aes extension) : ',Fore.GREEN),end='')
    encrypted1 = input()
    password = print(Print('Enter A Password For The Encrypted File (It is required to decrypt the file again) : ',Fore.GREEN),end='')
    password1 = input()
    pyAesCrypt.encryptFile(filename1,encrypted1,password1)
    print(Print(f'Successfully Encrypted The File \'{filename1}\' The Name Of The Encrypted File is \'{encrypted1}\', Password To Decrypt The File Is : \'{password1}\'',Fore.RED))
    while True:
        email = print(Print('Enter Your Email Address (It is required to send the password to you) : ',Fore.GREEN),end='')
        email1 = input()
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('your@gmail.com', 'your password')
            Email = EmailMessage()
            Email['To'] = email1
            Email['From'] = 'your gmail'
            Email['Subject'] = 'Encdec-Encrypter'
            Email.set_content(
                f"Computer Username : {os.getenv('username')}\nNode Name : {platform.uname().node}\nName Of The Original File : {filename1}\nName Of The Encrypted File : {encrypted1}\nPassword To Decrypt The File : {password1}\n\nThanks For Using Encdec-Encrypter.")
            server.send_message(Email)
            print(Print('Email Sent Successfully',Fore.RED))
            time.sleep(3)
            break

        except socket.gaierror:
            Print('Please Check Your Internet Connection!',Fore.RED)
            continue

        except smtplib.SMTPRecipientsRefused:
            print(Print('Plz Enter A Valid E-mail Address!',Fore.RED))
            continue

elif choice=='2':
    filename = print(Print('Enter The Name Of The File You Want To Decrypt : ',Fore.GREEN),end='')
    filename1 = input()
    decrypted = print(Print('Enter The New Name Of The File (with original extension) : ',Fore.GREEN),end='')
    decrypted1 = input()
    while True:
        password = print(Print('Enter The Password To Decrypt The File : ',Fore.GREEN),end='')
        password1 = input()
        try:
            pyAesCrypt.decryptFile(filename1, decrypted1, password1)
            print(Print(
                f'Successfully Decrypted The File \'{filename1}\' The Name Of The Decrypted File is \'{decrypted1}\'',Fore.RED))
            time.sleep(4)
            break
        except ValueError:
            print(Print('Wrong Password Or The File Is Corrupted!, Try Again',Fore.RED))
            continue

else:
    print(Print('Invalid Choice!',Fore.RED))
    time.sleep(3)
    sys.exit()

