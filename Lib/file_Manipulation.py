import os  # Provides functions to interact with the operating system
import json  # Allows working with JSON files (reading/writing)
import platform  # Used to determine the OS type
import subprocess  # Used to execute system commands

# Function to print the contents of a JSON file in a readable format
def Print_Json(file_path):
    try:
        with open(file_path, 'r') as f:  # Open the file in read mode
            data = json.load(f)  # Load JSON data from file
            print(json.dumps(data, indent=4))  # Pretty-print JSON data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")  # Handle missing file
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")  # Handle JSON errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Catch any other exceptions

# Function to list all files in a given directory
def List_Files_In_Directory(directory_path):
    try:
        files = os.listdir(directory_path)  # Get list of files in directory
        for file in files:
            full_path = os.path.join(directory_path, file)  # Get full file path
            if os.path.isfile(full_path):  # Check if it is a file
                print(file)  # Print the file name
    except FileNotFoundError:
        print(f"Error: Directory not found at {directory_path}")  # Handle missing directory
    except NotADirectoryError:
        print(f"Error: {directory_path} is not a directory.")  # Handle invalid directory
    except Exception as e:
        print(f"An error occurred: {e}")  # Catch any other exceptions

# Function to retrieve account information from a JSON file
def Get_Accounts(file_path):
    try:
        with open(file_path, 'r') as f:  # Open file in read mode
            data = json.load(f)  # Load JSON data
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict) and "account" in data[0]:
                return data[0]["account"]  # Return account if found
            else:
                return None  # Return None if structure is unexpected
    except FileNotFoundError:
        return None  # Return None if file is missing
    except json.JSONDecodeError:
        return None  # Return None if JSON format is invalid
    except Exception as e:
        print(f"An error occurred: {e}")  # Print any other error
        return None

# Function to print the contents of a log file
def Print_Logs(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Open file in read mode with UTF-8 encoding
            print(file.read())  # Read and print file contents
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")  # Handle missing file
    except Exception as e:
        print(f"An error occurred: {e}")  # Catch any other exceptions

# Function to delete a file
def Delete_File(fileName):
    if os.path.exists(fileName):  # Check if file exists
        os.remove(fileName)  # Delete the file
        print(f"File '{fileName}' has been deleted.")  # Confirm deletion
    else:
        print(f"File '{fileName}' not found.")  # Handle missing file

# Function to open a JSON file in VS Code
def Open_Editor(fileName):
    if not fileName.endswith(".json"):  # Ensure the file is JSON
        print("Error: Only JSON files are supported.")
        return
    if not os.path.exists(fileName):  # Check if file exists
        print(f"Error: File '{fileName}' not found.")
        return
    system_name = platform.system()  # Get the OS name
    try:
        if system_name in ["Windows", "Linux", "Darwin"]:  # Supported OS
            subprocess.run(["code", fileName], check=True)  # Open file in VS Code
        else:
            print(f"Unsupported OS: {system_name}")  # Handle unsupported OS
    except FileNotFoundError:
        print("Error: Could not run VS Code. Make sure VS Code is installed and in your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Error: VS Code returned an error. {e}")

# Function to save account credentials to a JSON file
def Save_Credentials(account, password, filepath):
    credentials = []  # Initialize credentials list
    filepath = os.path.abspath(filepath)  # Get absolute file path
    dir_path = os.path.dirname(filepath)  # Extract directory path
    if not os.path.exists(dir_path):  # Ensure directory exists
        try:
            os.makedirs(dir_path, exist_ok=True)  # Create directory if missing
        except OSError as e:
            print(f"Error creating directory {dir_path}: {e}")
            return
    if not os.path.isfile(filepath):  # If file doesn't exist, create an empty list
        try:
            with open(filepath, 'w') as jsonfile:
                json.dump([], jsonfile)
        except IOError as e:
            print(f"Error creating {filepath}: {e}")
            return
    try:
        with open(filepath, 'r') as jsonfile:  # Load existing data
            credentials = json.load(jsonfile)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error reading {filepath}: {e}")
        return
    credentials.append({'account': account, 'password': password})  # Add new credentials
    try:
        with open(filepath, 'w') as jsonfile:  # Save updated credentials
            json.dump(credentials, jsonfile, indent=4)
        print("Credentials saved successfully.")
    except IOError as e:
        print(f"Error writing to {filepath}: {e}")

# Function to create a session file with email details
def Create_Session(filename, subject, body, emails):
    filepath = filename + ".json"  # Construct file path
    data = [{  # Create data structure
        'subject': subject,
        'body': body,
        'emails': emails
    }]
    try:
        with open(filepath, 'w', encoding='utf-8') as jsonfile:  # Write data to file
            json.dump(data, jsonfile, indent=4)
        print(f"JSON file '{filename}.json' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
