import smtplib
import os
from email.message import EmailMessage

EMAIL_ADDRESS=os.environ.get('PYMAIL')
EMAIL_PASSWORD=os.environ.get('PYPASS')

def sendmsg(emailget,nameget):
    
    body=nameget+", you Have Signed Up!"
    message=EmailMessage()
    message['Subject']="Congratulations!"
    message['From']=EMAIL_ADDRESS
    message['To']=str(emailget)
    message.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)
