import re
import json


def Check_Account(json_string):
    try:
        data = json.loads(json_string)
        if "account" in data and data["account"] is not None:
            return True
        else:
            return False
    except json.JSONDecodeError:
        # Handle invalid JSON
        return False
    except TypeError:
        #Handle if the input is not a string.
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