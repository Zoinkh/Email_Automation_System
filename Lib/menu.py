
import check_Func
import logs
import file_Manipulation


def Menu():
    setting_Path = '\Data'
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
        user_Input = input(print('\tEnter Choice (1,2,3,4,0) : '))
        logs.Logs(f'{user_Input}_Status;Logged-in-Email={currentAccount}_Pending={scheduleEmail}')#log status : form json_ choices : user_iput
        if user_Input == 1:
            logs.Logs(f'User-Choosed=1.-New-Session')
            user_Input = ''
            user_Input = input(print('\tEnter New Session Name ( 0 to return): '))
            logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={user_Input}')
            if user_Input == 0:
                logs.Logs(f'User-Choosed_1.-New-Session_New-Session-Name={user_Input}_Back-to-Menu')
                return
            else :
                user_Input = ''
                while True: #loop enter email and save to Data/Save/fileName.csv
                    user_Input = ''
                    user_Input = input(print('\tEnter Receiver Email ( 0 to return | \'save\' to save): '))
                    logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email={user_Input}')
                    if user_Input == 0:
                        logs.Logs(f'User-Choosed_1.-New-Session_Receiver-Email={user_Input}_Back-to-Menu')
                        return
                    elif user_Input == 'save':
                        #create file in Data/Save/fileName.csv
                        return
                
        elif user_Input == 2:
            logs.Logs(f'User-Choosed=2.-Saved-Session')
            file_Manipulation.List_Files_In_Directory(saved_Session_Path)
            user_Input = ''  #list all saved session if mt print mt
            user_Input = input(print('\tEnter Session-Name ( 0 to return): '))
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
                user_Choice = input(print('\tEnter Choice : '))
                #if user_Choice == 1:
                    #loop through file length and send out email
                #elif user_Choice == 2:
                    #delete file
                #elif user_Choice == 3:
                    #file_Manipulation.Open_Editor(user_Input)
                
                    
                
        elif user_Input == 3:
            file_Manipulation.List_Files_In_Directory(logs_Path) #list all the logs
            while True:
                user_Input = ''
                user_Input = input(print('\tEnter log ID to read ( 0 to return): '))
                if user_Input == 0:
                    return
                else :
                    file_Manipulation.Print_Logs(user_Input)
        elif user_Input == 4:
            user_Input = ''
            user_Input = input(print('\tEnter your Email ( 0 to return): '))
            if user_Input == 0 :
                return
            elif check_Func.is_valid_email(user_Input):
                user_Input = ''
                user_Input = input(print('\tEnter your Password ( 0 to return): '))
                if user_Input == 0:
                    return
        elif user_Input == 0:
            print('Exiting')
            break
        else :
            print('invalid input!!!')

    
    
    

