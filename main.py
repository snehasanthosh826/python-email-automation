import os
import smtplib

# Sender and receiver email addresses
sender = "snehasanthosh360@gmail.com"
receiver = "sanjaysanthosh411@gmail.com"

# Read password from environment variable
password = os.environ.get("EMAIL_PASS")

# Check if password exists
if password is None:
    print("ERROR: EMAIL_PASS not found!")
    exit()

# Sample tasks for the report
tasks = [
    "Check logs",
    "Backup database",
    "Clear cache"
]

# Convert list to readable text
body = "\n".join(tasks)

# Create email message
message = f"""Subject: Daily Report

Hello,

Completed Tasks:

{body}

Regards,
Python Automation
"""

try:
    print("Connecting to Gmail...")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    print("Logging in...")

    server.login(sender, password)

    print("Sending email...")

    server.sendmail(
        sender,
        receiver,
        message
    )

    server.quit()

    print("Email sent successfully!")

except Exception as e:
    print("Error:", e)
 
