import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


    
def Send(sender_email, sender_password, receiver_email, subject, body):
    """
    Sends an email using Gmail's SMTP server.

    Args:
        sender_email (str): The sender's Gmail address.
        sender_password (str): The sender's Gmail password or app password.
        receiver_email (str): The recipient's email address.
        subject (str): The email subject.
        body (str): The email body (plain text )
    """

    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email 
    part = MIMEText(body, "plain")
    message.attach(part)
    # Create secure connection with server and send email
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

