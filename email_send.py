import smtplib
import os
import ssl

def send_email(message):

    host = 'smtp.gmail.com'
    port = 465
    user_name = 'asukhava@gmail.com'
    password = os.getenv("PASSWORD")
    receiver_email = 'asukhava@gmail.com'
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host,port,context=context) as email_server:
        email_server.login(user_name,password)
        email_server.sendmail(user_name,receiver_email,message)

if __name__ == "__main__":
    send_email("This is from direct run of this function file.")

