from email.message import EmailMessage
import os
import smtplib

def send_email(recipient):
    email_from = os.environ.get('EMAIL_ADDRESS')
    email_to = recipient

    smtp = "smtp.gmail.com"

    server = smtplib.SMTP(smtp, 587)
    server.starttls()
    server.login(email_from, os.environ.get('EMAIL_PASSWORD'))
    msg = "Teste de email"

    server.sendmail(email_from, email_to, msg)
    server.quit()

    print("Sucesso ao enviar email")
