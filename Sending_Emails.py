from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

message = MIMEMultipart()

message["from"] = "xxx@gmail.com"
message["to"] = "yyy@gmail.com"
message["subject"] = "TEST EMAIL - SENDING EMAIL WITH PYTHON."

message.attach(
    MIMEText("Hello, I'm trying out my Python sender, Regards.", "plain"))

# message.attach(MIMEImage(Path().read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("xxx@gmail.com", "")
    smtp.send_message(message)
    print("Sent...")
