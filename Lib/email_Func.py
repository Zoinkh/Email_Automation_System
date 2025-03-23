import json
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
        print(f"Email sent successfully to {receiver_email}!")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")



def Send_Email_Saved_Session(setting, session):
    """
    Reads sender credentials from a JSON file and email content from a JSON file, then sends emails.

    Args:
        setting (str): Path to the JSON file containing sender email and password.
        session (str): Path to the JSON file containing email subjects, bodies, and a list of recipient emails.
    """
    try:
        with open(setting, 'r', encoding='utf-8') as file1:
            sender_data = json.load(file1)
            sender_email = sender_data.get('send_email')
            sender_password = sender_data.get('sender_password')

            if not sender_email or not sender_password:
                print(f"Invalid sender credentials in {setting}.")
                return

        with open(session, 'r', encoding='utf-8') as file2:
            session_data = json.load(file2)
            emails = []
            for row in session_data:
                subject = row.get('subject')
                body = row.get('body')
                recipients = row.get('emails', [])  # Get the list of emails, default to [] if not present.

                if not isinstance(recipients, list):
                    print(f"Emails must be a list in session data: {row}")
                    continue # Skip to the next row

                for receiver_email in recipients:
                    if sender_email and sender_password and receiver_email and subject and body:
                        Send(sender_email, sender_password, receiver_email, subject, body)
                    else:
                        print("One or more email data is missing")

    except FileNotFoundError:
        print("One or both files not found.")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")