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

def send_emails_from_json_csv(setting, session):
    """
    Reads sender credentials from a JSON file and email content from a CSV file, then sends emails.

    Args:
        setting (str): Path to the JSON file containing sender email and password.
        session (str): Path to the CSV file containing email subjects, bodies, and recipient emails.
    """
    try:
        with open(setting, 'r', encoding='utf-8') as file1:
            sender_data = json.load(file1)
            sender_email = sender_data.get('send_email')
            sender_password = sender_data.get('sender_password')

            if not sender_email or not sender_password:
                print(f"Invalid sender credentials in {setting}.")
                return

        import csv
        with open(session, 'r', newline='', encoding='utf-8') as file2:
            reader2 = csv.DictReader(file2)
            emails = []
            for row2 in reader2:
                subject = row2.get('subject')
                body = row2.get('body')
                i = 0
                while True:
                    email_key = f'email{i}'
                    receiver_email = row2.get(email_key)
                    if receiver_email:
                        emails.append((receiver_email, subject, body))
                        i += 1
                    else:
                        break
            for receiver_email, subject, body in emails:
                if sender_email and sender_password and receiver_email and subject and body :
                    Send(sender_email, sender_password, receiver_email, subject, body)
                else:
                    print("One or more email data is missing")

    except FileNotFoundError:
        print("One or both files not found.")
    except json.JSONDecodeError:
        print(f"Invalid JSON format in {setting}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

