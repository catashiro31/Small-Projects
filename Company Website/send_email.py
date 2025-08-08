import smtplib, ssl
import os

def sending(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("USER")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("USER")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)

if __name__ == "__main__":
    sending(message="""\
    Subject: Hi!
    Check connect.
    """)
