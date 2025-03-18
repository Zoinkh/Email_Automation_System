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



def Create_Session(file_name, data):
    """
    Create a CSV file from the given data.
    
    :param file_name: Name of the CSV file to create (string)
    :param data: List of dictionaries containing the data to write
    """
    if not data:
        raise ValueError("Data cannot be empty")
    
    # Extract field names from the keys of the first dictionary
    field_names = data[0].keys()
    
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)
    print(f"CSV file '{file_name}' created successfully.")


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

