import os
import sys
lib_path = os.path.abspath('Lib')
sys.path.append(lib_path)
import logs
import file_Manipulation
import email_Func
import check_Func

def Menu():
    setting_Path = "Data/setting.json"
    logs_Path = "Logs"
    saved_Session_Path = "Data/Saved/"
 
    while True:
        if check_Func.file_exists(setting_Path):
            currentAccount = file_Manipulation.Get_Accounts(setting_Path)
            print(f'\tStatus :\nLogged in Email :{currentAccount}') 
            
        print('''\t********** Menu **********\n
              \t1. New Session\n
              \t2. Saved Session\n
              \t3. Logs\n
              \t4. Email Account\n
              \t0. Exit\n''')
        user_Input = ''
        user_Input = input('\tEnter Choice (1,2,3,4,0) : ')
        logs.Logs(f'{user_Input}_Status;Logged-in-Email={currentAccount}')
        if user_Input == '1':
            logs.Logs(f'User-Choosed=1.-New-Session')
            session_Name = ''
            session_Name = input('\tEnter New Session Name ( 0 to Exit): ')
            logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}')
            if user_Input == '0':
                logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}_Back-to-Menu')
                Menu()
            subject_email = ''
            subject_email = input('\tEnter Subject ( 0 to Exit): ')
            if user_Input == '0':
                logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}_Subject={subject_email}')
                Menu()
            body_email = ''
            body_email = input('\tEnter Messages ( 0 to Exit): ')
            if user_Input == '0':
                logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}_Body={body_email}')
                Menu()
            email_Input = []
            while True:
                user_Input = input('\tEnter Receiver Email (\'save\' to save): ')
                if user_Input == '0':
                    logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email={user_Input}_Back-to-Menu')
                    Menu()
                if user_Input == 'save':
                    file_Manipulation.Create_Session(saved_Session_Path + session_Name,subject_email,body_email,email_Input)
                    logs.Logs(f'Saved Session_Path:{saved_Session_Path}_Name:{session_Name}_Subject-Email:{subject_email}_Body-Email:{body_email},Reciever:{email_Input}')
                    user_Input = ''
                    user_Input = input('\t1. Send \n\t0. Back to menu\n\tEnter Choice : ')
                    if user_Input == '1':
                        email_Func.Send_Email_Saved_Session(setting_Path,saved_Session_Path + session_Name + '.json')
                        logs.Logs(f'Created-Session_Prompt:1.-Send-User:_Name:{session_Name}_Subject-Email:{subject_email}_Body-Email:{body_email},Reciever:{email_Input}')
                    elif user_Input == '2':
                            if user_Input == '0':
                                Menu()
                                logs.Logs(f'Created-Session_Prompt:Exite-back-to-menu')
                            else :
                                print('invalid input!')   
                    elif user_Input =='0':
                        Menu()
                    else :
                        print('invalid input!') 
                        logs.Logs(f'Created-Session_Prompt:Invalid-Input:{user_Input}')
                if check_Func.is_valid_email(user_Input):
                    logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email={user_Input}')
                    email_Input.append(user_Input)
                else:
                    print('invalid Email')
                    logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email_Invalid-input:{user_Input}')
        elif user_Input == '2':
            logs.Logs(f'User-Choosed=2.-Saved-Session')
            file_Manipulation.List_Files_In_Directory(saved_Session_Path) #list all saved session if mt print mt
            user_Input = ''  
            user_Input = input('\tEnter Session-Name ( 0 to Menu()): ')
            logs.Logs(f'User-Choosed=2.-Saved-Session_Open-Session={user_Input}') 
            if user_Input == '0':
                logs.Logs(f'User-Choosed=2.-Saved-Session_Exit-back-to-Menu')
                Menu()
            else:
                file_Manipulation.Print_Json(saved_Session_Path+user_Input+'.json')
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
                
        elif user_Input == '3':
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
        elif user_Input == '4':
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
                
        elif user_Input == '0':
            print('Exiting')
            logs.Logs('exit-program')
            exit()
        else :
            print('invalid input!')
            logs.Logs(f'Menu_Invalid-Input:{user_Input}')
   

