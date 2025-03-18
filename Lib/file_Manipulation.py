import csv
import os
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
        
        

def list_files_in_directory(directory_path):
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

