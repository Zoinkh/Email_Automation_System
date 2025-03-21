
import check_Func
import logs
import file_Manipulation
import email_Func

def Menu():
    setting_Path = '\Data/setting.json'
    logs_Path = '\Logs'
    saved_Session_Path = '\Data/Saved'
    currentAccount = file_Manipulation.Get_Accounts(setting_Path)
    scheduleEmail ='' # load time form csv file and calcualte time left
        
        
    while True:
      
        user_Input = 0
        if check_Func.check("\Data/setting.json"):
            print(f'''\tStatus :\nLogged in Email :{currentAccount}
                        \nPending: {scheduleEmail}  ''') # check if email is already sing in if in print out email else ask to sing in
            #show pending sehculd email to send out
        print('''********** Menu **********\n
              \t1. New Session\n
              \t2. Saved Session\n
              \t3. Logs\n
              \t4. Email Account\n
              \t0. Exit\n''')
        user_Input = input('\tEnter Choice (1,2,3,4,0) : ')
        logs.Logs(f'{user_Input}_Status;Logged-in-Email={currentAccount}_Pending={scheduleEmail}')#log status : form json_ choices : user_iput
        if user_Input == 1:
            logs.Logs(f'User-Choosed=1.-New-Session')
            session_Name = ''
            session_Name = input('\tEnter New Session Name ( 0 to return): ')
            logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}')
            if user_Input == 0:
                logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={session_Name}_Back-to-Menu')
                return
            message = ''
            message = input('\tEnter New Session Name ( 0 to return): ')
            emial_Input = []
            while True:
                user_input = input('\tEnter Receiver Email (\'save\' to save): ')
                logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email={user_Input}')
                if user_input.lower() == 'save':
                    break
                emial_Input.append(user_input)
                file_Manipulation.Create_Session(saved_Session_Path+session_Name,message,emial_Input)
            if user_Input == 0:
                logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email={user_Input}_Back-to-Menu')
                return
                
        elif user_Input == 2:
            logs.Logs(f'User-Choosed=2.-Saved-Session')
            file_Manipulation.List_Files_In_Directory(saved_Session_Path) #list all saved session if mt print mt
            user_Input = ''  
            user_Input = input('\tEnter Session-Name ( 0 to return): ')
            logs.Logs(f'User-Choosed=2.-Saved-Session_Open-Session={user_Input}') 
            if user_Input == 0:
                logs.Logs(f'User-Choosed=2.-Saved-Session_Exit-back-to-Menu')
                return
            else:
                file_Manipulation.Print_CSV(user_Input)
                print('''********** Options ***********\n
                      \t1. Send Session
                      \t2. Delete Session
                      \t3. Edit Session (Notepad/Nano)
                      \t0. Exite back to Menu''')   # check os for which to open
                #print out saved session
                #promte to for set time and and edit
                user_Choice = ''
                user_Choice = input('\tEnter Choice : ')
                if user_Choice == 1:
                    email_Func.Send_Emails_From_Saved_Session(setting_Path,saved_Session_Path + user_Input+'.json')
                elif user_Choice == 2:
                    file_Manipulation.Delete_File(user_Input)
                elif user_Choice == 3:
                    file_Manipulation.Open_Editor(user_Input)
                
                    
                
        elif user_Input == 3:
            file_Manipulation.List_Files_In_Directory(logs_Path) #list all the logs
            while True:
                user_Input = ''
                user_Input = input('\tEnter log ID to read ( 0 to return): ')
                if user_Input == 0:
                    return
                else :
                    file_Manipulation.Print_Logs(user_Input)
        elif user_Input == 4:
            user_Input = ''
            user_Input = input('\tEnter your Email ( 0 to return): ')
            if user_Input == 0 :
                return
            elif check_Func.is_valid_email(user_Input):
                user_Input0 = ''
                user_Input0 = input('\tEnter your Password ( 0 to return): ')
                if user_Input0 == 0:
                    return
                else:
                
                    file_Manipulation.Save_Account(str(user_Input),str(user_Input0),setting_Path+'.json')
            else:
                print('invalid Email!!!')
                
                    
        elif user_Input == 0:
            print('Exiting')
            break
        else :
            print('invalid input!')    
    
    

