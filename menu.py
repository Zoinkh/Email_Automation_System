import os # Import the os module for operating system interactions.
import sys # Import the sys module for system-specific parameters and functions.
lib_path = os.path.abspath('Lib') # Define the path to the 'Lib' directory.
sys.path.append(lib_path) # Add the 'Lib' directory to the Python path.
import logs # Import the 'logs' module for logging functionality.
import file_Manipulation # Import the 'file_Manipulation' module for file handling.
import email_Func # Import the 'email_Func' module for email functions.
import check_Func # Import the 'check_Func' module for validation checks.

def Menu(): # Define the main function 'Menu'.
    setting_Path = "Data/setting.json" # Set the path for the settings file.
    logs_Path = "Logs" # Set the path for the logs directory.
    saved_Session_Path = "Data/Saved/" # Set the path for saved sessions.
 
    while True: # Start an infinite loop to keep the menu running.
        if check_Func.file_exists(setting_Path): # Check if the settings file exists.
            currentAccount = file_Manipulation.Get_Accounts(setting_Path) # Get the current account from the settings file.
            print(f'\tStatus :\nLogged in Email :{currentAccount}') # Print the logged-in email.
            
        print('''\t********** Menu **********\n # Print the main menu options.
              \t1. New Session\n
              \t2. Saved Session\n
              \t3. Logs\n
              \t4. Email Account\n
              \t0. Exit\n''')
        user_Input = '' # Initialize user input variable.
        user_Input = input('\tEnter Choice (1,2,3,4,0) : ') # Get user's menu choice.
        logs.Logs(f'{user_Input}_Status;Logged-in-Email={currentAccount}') # Log the user's menu choice.
        if user_Input == '1': # If user chooses '1' (New Session).
            logs.Logs(f'User-Choosed=1.-New-Session') # Log the start of a new session.
            session_Name = '' # Initialize session name variable.
            session_Name = input('\tEnter New Session Name ( 0 to Exit): ') # Get the new session name.
            logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}') # Log the session name.
            if user_Input == '0': # If user enters '0' to exit.
                logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}_Back-to-Menu') # Log the exit.
                Menu() # Return to the main menu.
            subject_email = '' # Initialize subject email variable.
            subject_email = input('\tEnter Subject ( 0 to Exit): ') # Get the email subject.
            if user_Input == '0': # If user enters '0' to exit.
                logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}_Subject={subject_email}') # Log the exit.
                Menu() # Return to the main menu.
            body_email = '' # Initialize email body variable
            body_email = input('\tEnter Messages ( 0 to Exit): ') # Get the email body.
            if user_Input == '0': # If user enters '0' to exit.
                logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}_Body={body_email}') # Log the exit
                Menu() # Return to the main menu.
            email_Input = [] # Initialize the list of recipient emails.
            while True: # Start a loop to get recipient emails.
                user_Input = input('\tEnter Receiver Email (\'save\' to save): ') # Get an email address.
                if user_Input == '0': # If user enters '0' to exit.
                    logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email={user_Input}_Back-to-Menu') # Log the exit.
                    Menu() # Return to the main menu.
                if user_Input == 'save': # If user enters 'save' to save the session.
                    file_Manipulation.Create_Session(saved_Session_Path + session_Name,subject_email,body_email,email_Input) # Create and save the session.
                    logs.Logs(f'Saved Session_Path:{saved_Session_Path}_Name:{session_Name}_Subject-Email:{subject_email}_Body-Email:{body_email},Reciever:{email_Input}') # Log the saved session.
                    user_Input = '' # Clear user input.
                    user_Input = input('\t1. Send \n\t0. Back to menu\n\tEnter Choice : ') # Ask user to send or go back.
                    if user_Input == '1': # If user chooses '1' to send.
                        email_Func.Send_Email_Saved_Session(setting_Path,saved_Session_Path + session_Name + '.json') # Send the email.
                        logs.Logs(f'Created-Session_Prompt:1.-Send-User:_Name:{session_Name}_Subject-Email:{subject_email}_Body-Email:{body_email},Reciever:{email_Input}') # Log the sending.
                    elif user_Input == '2':
                            if user_Input == '0':
                                Menu()
                                logs.Logs(f'Created-Session_Prompt:Exite-back-to-menu')
                            else :
                                print('invalid input!')   
                    elif user_Input =='0': #if user chooses 0
                        Menu()
                    else :
                        print('invalid input!') #error message
                        logs.Logs(f'Created-Session_Prompt:Invalid-Input:{user_Input}') #log error
                if check_Func.is_valid_email(user_Input): # Check if the email is valid.
                    logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email={user_Input}') # Log the valid email.
                    email_Input.append(user_Input) # Add the email to the list.
                else: # If the email is invalid.
                    print('invalid Email') # Print an error message.
                    logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email_Invalid-input:{user_Input}') # Log the invalid email.
        elif user_Input == '2': # If user chooses '2' (Saved Session).
            logs.Logs(f'User-Choosed=2.-Saved-Session') # Log the choice.
            file_Manipulation.List_Files_In_Directory(saved_Session_Path) # List saved sessions.
            user_Input = '' # Clear user input
            user_Input = input('\tEnter Session-Name ( 0 to Menu()): ') # Get session name.
            logs.Logs(f'User-Choosed=2.-Saved-Session_Open-Session={user_Input}') # Log the session name.
            if user_Input == '0': # If user enters '0' to exit.
                logs.Logs(f'User-Choosed=2.-Saved-Session_Exit-back-to-Menu') # Log the exit.
                Menu() # Return to the main menu.
            else: # If a session name is entered.
                file_Manipulation.Print_Json(saved_Session_Path+user_Input+'.json') # Print the session details.
                print('''\t********** Options ***********\n
                      \t1. Send Session
                      \t2. Delete Session
                      \t3. Edit Session
                      \t0. Exite back to Menu''')   # check os for which to open
                #print out saved session
                #promte to for set time and and edit
                user_Choice = ''
                user_Choice = input('\tEnter Choice : ')
                if user_Choice == '1':
                    email_Func.Send_Email_Saved_Session(setting_Path,saved_Session_Path + user_Input + '.json')
                    Menu()
                elif user_Choice == '2':
                    file_Manipulation.Delete_File(saved_Session_Path+user_Input+'.json')
                    logs.Logs(f'User-Choosed=2.-Saved-Session_Open-Session={user_Input}_Delete-session')
                elif user_Choice == '3':
                    file_Manipulation.Open_Editor(saved_Session_Path+user_Input+'.json')
                    logs.Logs(f'User-Choosed=2.-Saved-Session_Open-Session={user_Input}_Open-file-editor')
                else:
                    print('invalid input')
                    logs.Logs(f'User-Choosed=2.-Saved-Session_Open-Session={user_Input}_Invalid-Input:{user_Choice}')
                
        elif user_Input == '3': # If user chooses '3' (Logs).
            file_Manipulation.List_Files_In_Directory(logs_Path) #list all the logs
            while True:
                user_Input = ''
                user_Input = input('\tEnter log Date(dd-mm-yy) to read ( 0 to Exit): ')
                logs.Logs(f'User-choice:3_3.-Log_Log-File-Name:{user_Input}')
                if user_Input == '0':
                    logs.Logs(f'User-choice:3_3.-Log_User_choice:0_Exit-back-to-meu')
                    Menu()
                else :
                    file_Manipulation.Print_Logs(logs_Path+'/'+user_Input+'.txt')
                    logs.Logs(f'User-choice:3_3.-Log_Log-File-Name:{logs_Path+'/'+user_Input+'.txt'}_Print-Log-out')
        elif user_Input == '4': # If user chooses '4' (Email Account).
            user_Input = ''
            user_Input = input('\tEnter your Email ( 0 to Exit): ')
            if user_Input == '0' :
                logs.Logs(f'User-choice:4_4.-Sing-in-Email_Email:{user_Input}')
                Menu()
            elif check_Func.is_valid_email(user_Input):
                user_Input0 = ''
                user_Input0 = input('\tEnter your Password ( 0 to Exit): ')
                if user_Input0 == '0':
                    logs.Logs(f'User-choice:4_4.-Sing-in-Email:0_Exit-back-to-meu')
                    Menu()
                file_Manipulation.Save_Credentials(user_Input,user_Input0,setting_Path)
                Menu()
            else:
                logs.Logs(f'User-choice:4_4.-Sing-in-Email_Email-Invalid-input:{user_Input}')
                print('invalid Email!!!')
                
        elif user_Input == '0': # If user chooses '0' (Exit).
            print('Exiting') # Print exit message.
            logs.Logs('exit-program') # Log the program exit.
            exit() # Exit the program.
        else : # If the user enters an invalid input.
            print('invalid input!') # Print an error message.
            logs.Logs(f'Menu_Invalid-Input:{user_Input}') # Log the invalid input.

