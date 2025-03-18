import os
from datetime import datetime
def Logs(info):
    now = datetime.now()
    current_Datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    log_Name_Datetime = now.strftime("%d-%m-%Y")
    file_Name = f"Logs/{log_Name_Datetime}.txt"
    with open(file_Name, "a") as file:
        file.write(f"{current_Datetime} - {info}\n")
    file.close()