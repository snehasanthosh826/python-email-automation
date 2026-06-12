import smtplib
import os

sender = "snehasanthosh360@gmail.com"
receiver = "Sanjaysanthosh411@gmail.com"

password = os.environ.get("EMAIL_PASS")
message = """
Subject: Test Email

Hello!

This email was sent using Python.
"""

server = smtplib.SMTP(
    "smtp.gmail.com",
    587
)

server.starttls()

server.login(
    sender,
    password
)

server.sendmail(
    sender,
    receiver,
    message
)

server.quit()

print("Email sent successfully!")