import os  # Import the os module  
from datetime import datetime  # Import datetime for working with dates and times  

def Logs(info):  # Define the Logs function  
    now = datetime.now()  # Get the current date and time  
    current_Datetime = now.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time  
    log_Name_Datetime = now.strftime("%d-%m-%Y")  # Format the date for the log filename  
    file_Name = f"Logs/{log_Name_Datetime}.txt"  # Create the log file path  

    with open(file_Name, "a") as file:  # Open the file in append mode  
        file.write(f"{current_Datetime} - {info}\n")  # Write log entry  
        
    file.close()  # Close the file 
