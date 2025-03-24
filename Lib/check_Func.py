import re
import os


def file_exists(path):
  """
  Checks if a file exists at the given path.

  Args:
    path: The path to the file.

  Returns:
    True if the file exists, False otherwise.
  """
  return os.path.isfile(path)
    
def is_valid_time(time_str):
    """
    Checks if a string is in the "HH:MM:SS" format.

    Args:
        time_str (str): The string to check.

    Returns:
        bool: True if the string is in the correct format, False otherwise.
    """
    pattern = r"^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$"
    return bool(re.match(pattern, time_str))
    
    
    


def is_valid_email(email):
    if not isinstance(email, str):
        return False #Return false if input is not a string.

    # Regular expression for a basic email validation
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(email_regex, email):
        return True
    else:
        return False