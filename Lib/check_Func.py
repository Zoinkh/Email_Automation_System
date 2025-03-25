import re  # Import the regular expression module for pattern matching.
import os  # Import the operating system module for file system operations.


def file_exists(path):
  """
  Checks if a file exists at the given path.

  Args:
    path: The path to the file.

  Returns:
    True if the file exists, False otherwise.
  """
  return os.path.isfile(path) # Returns True if the path points to a regular file, false otherwise.
    
def is_valid_email(email):
    """
    Checks if a given string is a valid email address.

    Args:
      email: The string to check.

    Returns:
      True if the string is a valid email, False otherwise.
    """
    if not isinstance(email, str):
        return False #Return false if input is not a string.

    # Regular expression for a basic email validation
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" #Defines a regular expression pattern for basic email structure.

    if re.match(email_regex, email): #Checks if the provided email string matches the regular expression.
        return True #Returns true if it matches.
    else:
        return False #Returns false if it does not match.