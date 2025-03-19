import csv
import os
import json
import platform
import subprocess
 # probaly need add func to add csv file
#def new_Session():
    #take name email and message and save to .csv file
    


def Print_CSV(filepath):
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                print(row) # or print(','.join(row)) to print comma separated.

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        

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
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data.get("accounts", [])  # Return accounts list if exists, else empty list
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        return []


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
    """Opens a CSV file with the appropriate editor based on the OS."""
    if not fileName.endswith(".csv"):
        print("Error: Only CSV files are supported.")
        return

    system_name = platform.system()

    try:
        if system_name == "Windows":
            subprocess.run(["notepad", fileName], check=True)
        elif system_name == "Linux":
            subprocess.run(["vi", fileName], check=True)
        else:
            print(f"Unsupported OS: {system_name}")
    except FileNotFoundError:
        print("Error: Could not open file. Make sure the editor is installed.")




def Save_Credentials(account, password, filepath):
    """
    Saves account and password credentials to a CSV file.

    Args:
        account: The account name.
        password: The password.
        filepath: The path to the CSV file (default: 'settings.csv').
    """
    fieldnames = ['account', 'password']

    file_exists = os.path.isfile(filepath)

    try:
        with open(filepath, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({'account': account, 'password': password})
    except IOError as e:
        print(f"Error writing to {filepath}: {e}")



def Create_Session(filename, message, emails):
    """
    Creates a CSV file with message and email addresses.

    Args:
        filename (str): The name of the CSV file to create.
        message (str): The message to include in the CSV.
        emails (list): A list of email addresses.
    """
    fieldnames = ['message']
    for i, email in enumerate(emails):
        fieldnames.append(f'email{i+1}')

    data = {'message': message}
    for i, email in enumerate(emails):
        data[f'email{i+1}'] = email

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(data)

        print(f"CSV file '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
