import json
import check_Func
import logs
import file_Manipulation


def Menu():
    while True:
        
        user_Input = 0
        if check_Func.check("\Data/setting.json"):
            print('Status : ') # check if email is already sing in if in print out email else ask to sing in
        print('********** Menu **********\n')
        print('\t1. New Session\n')
        print('\t2. Saved Session\n')
        print('\t3. Logs')
        print('\t4. Email Account\n')
        print('\t0. Exit\n')
        user_Input = input(print('\tEnter Choice (1,2,3,4,0) : '))
        logs.Logs(f'{user_Input}_Status: Current Account:')#log status : form json_ choices : user_iput
        if user_Input == 1:
            user_Input = ''
            user_Input = input(print('\tEnter New Session Name ( 0 to return): '))
            if user_Input == 0:
                return
            else :
                user_Input = ''
                while True: #loop enter email and save to Data/Save/fileName.csv
                    user_Input = ''
                    user_Input = input(print('\tEnter Receiver Email ( 0 to return): '))
                    if user_Input == 0:
                        return
                    elif user_Input == 'save':
                        #create file in Data/Save/fileName.csv
                        return
                
        elif user_Input == 2:
            user_Input = ''  #list all saved session if mt print mt
            user_Input = input(print('\tEnter Session-Name ( 0 to return): '))
           
        elif user_Input == 3:
            file_Manipulation.list_files_in_directory('\Logs') #list all the logs
            while True:
                user_Input = ''
                user_Input = input(print('\tEnter log ID to read ( 0 to return): '))
                if user_Input == 0:
                    return
                else :
                    #print of Datetime.log out
        elif user_Input == 4:
             user_Input = ''
             user_Input = input(print('\tEnter your Email ( 0 to return): '))
            if user_Input == 0:
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

    
