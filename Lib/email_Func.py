import json  # Imports the json module for working with JSON data.
import smtplib  # Imports the smtplib module for sending emails using SMTP.
import ssl  # Imports the ssl module for secure connections (TLS/SSL).
from email.mime.text import MIMEText  # Imports MIMEText for creating plain text email bodies.
from email.mime.multipart import MIMEMultipart  # Imports MIMEMultipart for creating multipart email messages.

def Send(sender_email, sender_password, receiver_email, subject, body):
    """
    Sends an email.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        receiver_email (str): The recipient's email address.
        subject (str): The email subject.
        body (str): The email body.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    message = MIMEMultipart("alternative")  # Creates a multipart message object.
    message["Subject"] = subject  # Sets the email subject.
    message["From"] = sender_email  # Sets the sender's email address.
    message["To"] = receiver_email  # Sets the recipient's email address.

    part = MIMEText(body, "plain")  # Creates a plain text part for the email body.
    message.attach(part)  # Attaches the body to the message.

    try:
        # Use port 587 and starttls() for Gmail
        with smtplib.SMTP("smtp.gmail.com", 587) as server:  # Creates an SMTP connection to Gmail's server on port 587.
            server.starttls()  # Secures the connection using TLS.
            server.login(sender_email, sender_password)  # Logs in to the sender's email account.
            server.sendmail(sender_email, receiver_email, message.as_string())  # Sends the email.
        print(f"Email sent successfully to {receiver_email}!")  # Prints a success message.
        return True  # Returns True to indicate success.
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")  # Prints an error message.
        return False  # Returns False to indicate failure.

def Send_Email_Saved_Session(setting, session):
    """
    Sends emails based on data from saved JSON files.

    Args:
        setting (str): The path to the JSON file containing sender credentials.
        session (str): The path to the JSON file containing email data (recipients, subject, body).
    """
    try:
        with open(setting, 'r', encoding='utf-8') as file1:  # Opens the sender settings file in read mode.
            sender_data = json.load(file1)  # Loads the JSON data from the file.
            # The JSON in 'setting' is a list containing a dictionary. Access it correctly:
            sender_email = sender_data[0].get('account')  # Extracts the sender's email address.
            sender_password = sender_data[0].get('password')  # Extracts the sender's password.

            if not sender_email or not sender_password:
                print(f"Invalid sender credentials in {setting}.") #Handles if credentials are missing.
                return

        with open(session, 'r', encoding='utf-8') as file2:  # Opens the session data file in read mode.
            session_data = json.load(file2)  # Loads the JSON data from the file.
            emails = [] #Creates an empty list. Not used.
            all_emails_sent_successfully = True # Assume all emails will be sent successfully
            for row in session_data:  # Iterates through each email entry in the session data.
                subject = row.get('subject')  # Extracts the email subject.
                body = row.get('body')  # Extracts the email body.
                recipients = row.get('emails',)  # Gets the list of recipient emails.

                if not isinstance(recipients, list):
                    print(f"Emails must be a list in session data: {row}")
                    continue # Skip to the next row

                for receiver_email in recipients:  # Iterates through each recipient email.
                    if sender_email and sender_password and receiver_email and subject and body:  # Checks if all required data is present.
                        if not Send(sender_email, sender_password, receiver_email, subject, body): #Call the send function.
                            all_emails_sent_successfully = False # If any email send fails, change the flag
                    else:
                        print("One or more email data is missing") #Handles missing data.
            if all_emails_sent_successfully:
                print("All emails in the session were sent successfully!")
            else:
                print("One or more emails failed to send.")

    except FileNotFoundError:
        print("One or both files not found.")  # Handles the case where the file(s) are not found.
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")  # Handles JSON decoding errors.
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Handles other unexpected errors.