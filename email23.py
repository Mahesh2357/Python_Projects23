import email
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


print('hello email...\n')

print('Welcome to the Email Marketing.\n')
#! this can be read from csv.

emailist = ['xysr5050@gmail.com', 'ttyuzw1938@gmail.com', 'aaabbbccc2357@gmail.com']

def sendMail(fromEmail, toEmail, subject, message):
    msg = MIMEMultipart()
    msg.set_unixfrom('MAHESH')
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = subject
    msg['Message'] = message
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
    mailserver.ehlo()
    mailserver.login(os.environ['email'] , os.environ['password'])
    mailserver.sendmail(fromEmail, toEmail, msg.as_string())
    mailserver.quit()

    
    
for email in emailist:
    fromEmail = 'maheshmungase1938@gmail.com'
    subject = 'hii......butterfly is arrived.....'
    message = 'mmzf@83'
    # sendMail(fromEmail, subject, message)

    print(f'Mail sent to - {email}')
    time.sleep(3)
print('\n')
print('Mails sent successfully...')



