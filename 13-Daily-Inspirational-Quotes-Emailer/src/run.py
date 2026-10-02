import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_simple_email(sender, recipient, subject, body):
    # Create the email content
    msg = MIMEText(body)  # msg is an object from MIMEText type.
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Set up the SMTP server
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "your_email@gmail.com"
    password = "your_password"

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


# Usage
send_simple_email(
    "sender@example.com",
    "recipient@example.com",
    "Hello from Python",
    "This is a simple text email sent from Python."
)



