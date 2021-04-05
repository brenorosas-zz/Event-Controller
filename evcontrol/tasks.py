from email.message import EmailMessage
import os
import smtplib

def send_email(recipient, event):
    try:
        msg = EmailMessage()
        msg['Subject'] = ("Invite to event: " + event.title)
        msg.set_content("{}\n\n Date : {}".format(event.description, event.date))
        msg['From'] = os.environ.get('EMAIL_ADDRESS')
        msg['To'] = recipient
        smtp = "smtp.gmail.com"
        server = smtplib.SMTP_SSL(smtp, 465)
        server.login(os.environ.get('EMAIL_ADDRESS'), os.environ.get('EMAIL_PASSWORD'))
        server.send_message(msg)
        server.quit()
        print("Sucesso ao enviar email")
    except:
        return False

    return True
