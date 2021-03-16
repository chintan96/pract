from pract.celery import app
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

@app.task(name="send_email_image")
def send_email_image(sender_email,receiver_email,'filename'):
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "COVID DATA IMAGE FILE"
    password = "*********"
    ##############################################################
    ##Please enter your password here, alse check senders' and receivers' email id##
    ##############################################################
    message.attach(MIMEText("Please Find Attached", "plain"))
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition",f"attachment; filename= {filename}")
    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
