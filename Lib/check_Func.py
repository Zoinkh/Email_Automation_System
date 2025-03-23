import re
import json
import os


def Check_Account(file_path):
    if not os.path.exists(file_path):
        return False  # File does not exist
    
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        
        if "account" in data and data["account"] is not None:
            return True
        else:
            return False
    except json.JSONDecodeError:
        # Handle invalid JSON
        return False
    except (TypeError, IOError):
        # Handle if the input is not a valid file or cannot be read
        return False

    
    
    


def is_valid_email(email):
    if not isinstance(email, str):
        return False #Return false if input is not a string.

    # Regular expression for a basic email validation
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(email_regex, email):
        return True
    else:
        return False