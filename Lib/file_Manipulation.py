import os
import json
import platform
import subprocess
 # probaly need add func to add csv file
#def new_Session():
    #take name email and body and save to .csv file
    


def Print_Json(file_path):
    """
    Reads a JSON file and prints its contents in a formatted way.

    Args:
        file_path (str): The path to the JSON file.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            print(json.dumps(data, indent=4))  # Use indent for pretty printing

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def List_Files_In_Directory(directory_path):
    try:
        files = os.listdir(directory_path)
        for file in files:
            full_path = os.path.join(directory_path, file)
            if os.path.isfile(full_path): # Check if it's a file, not a directory.
                print(file)

    except FileNotFoundError:
        print(f"Error: Directory not found at {directory_path}")
    except NotADirectoryError:
        print(f"Error: {directory_path} is not a directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

def Get_Accounts(file_path):
    """
    Extracts the 'account' value from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        str: The value of the 'account' key, or None if not found or an error occurs.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict) and "account" in data[0]:
                return data[0]["account"]
            else:
                return None  # Return None if the JSON structure is unexpected
    except FileNotFoundError:
        return None  # Return None if the file is not found
    except json.JSONDecodeError:
        return None # Return None if the file is not valid Json.
    except Exception as e:
        print(f"An error occurred: {e}") # Print any other exception.
        return None




def Print_Logs(file_path):
    """Prints the contents of a .txt file given its path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")




def Delete_File(fileName):
    """Deletes the specified file if it exists."""
    if os.path.exists(fileName):
        os.remove(fileName)
        print(f"File '{fileName}' has been deleted.")
    else:
        print(f"File '{fileName}' not found.")


def Open_Editor(fileName):
    """Opens a JSON file with VS Code based on the OS."""
    if not fileName.endswith(".json"):
        print("Error: Only JSON files are supported.")
        return

    if not os.path.exists(fileName):
        print(f"Error: File '{fileName}' not found.")
        return

    system_name = platform.system()

    try:
        if system_name == "Windows":
            subprocess.run(["code", fileName], check=True)
        elif system_name == "Linux":
            subprocess.run(["code", fileName], check=True)
        elif system_name == "Darwin": # macOS
            subprocess.run(["code", fileName], check=True)
        else:
            print(f"Unsupported OS: {system_name}")
    except FileNotFoundError:
        print("Error: Could not run VS Code. Make sure VS Code is installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error: VS Code returned an error. {e}")



def Save_Credentials(account, password, filepath):
    """
    Saves account and password credentials to a JSON file.

    Args:
        account: The account name.
        password: The password.
        filepath: The path to the JSON file (default: 'setting.json').
    """
    credentials = []
    
    # Get absolute directory path
    filepath = os.path.abspath(filepath)
    dir_path = os.path.dirname(filepath)
    
    # Ensure the directory exists
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path, exist_ok=True)
        except OSError as e:
            print(f"Error creating directory {dir_path}: {e}")
            return
    
    # Check if the file exists, if not create one with an empty list
    if not os.path.isfile(filepath):
        try:
            with open(filepath, 'w') as jsonfile:
                json.dump([], jsonfile)
        except IOError as e:
            print(f"Error creating {filepath}: {e}")
            return
    
    # Load existing data
    try:
        with open(filepath, 'r') as jsonfile:
            credentials = json.load(jsonfile)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading {filepath}: {e}")
        return
    
    # Append new credentials
    credentials.append({'account': account, 'password': password})
    
    # Save updated credentials to JSON file
    try:
        with open(filepath, 'w') as jsonfile:
            json.dump(credentials, jsonfile, indent=4)
        print("Credentials saved successfully.")  # Print success body
    except IOError as e:
        print(f"Error writing to {filepath}: {e}")




def Create_Session(filename, subject, body, emails):
    """
    Creates a JSON file with subject, body, and a list of email addresses.

    Args:
        filename (str): The name of the JSON file to create (without .json extension).
        subject (str): The subject of the body.
        body (str): The body to include in the JSON.
        emails (list): A list of email addresses.
    """
    filepath = filename + ".json" # Simplified path creation

    # Create the structure as a list of dictionaries, because the send function expects that.
    data = [{
        'subject': subject,
        'body': body,
        'emails': emails
    }]

    try:
        with open(filepath, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)  # Use indent for better readability

        print(f"JSON file '{filename}.json' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")




