import re
import os


def file_exists(path):
  return os.path.isfile(path)
    
def is_valid_email(email):
    if not isinstance(email, str):
        return False #Return false if input is not a string.

    # Regular expression for a basic email validation
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(email_regex, email):
        return True
    else:
        return False