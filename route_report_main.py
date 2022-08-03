
import glob
import shutil, os
from pathlib import Path


from datetime import datetime
import sys
import route_report_download
import route_report_convert
import route_report_mail
import route_report_alarms

program_successful = False
user_select_date = ""
user_select_time = ""
main_user_date = ""
main_user_time = ""

print("What should I do?\n1.Download Today's Route Report?\n2.Convert Report?\n3.Add alarms?\n4.Send Route Report Email?\n5.Quit?\n")

user_input = int(input('>'))

user_date = ''

user_time = ''


if user_input == 5:
    print("\nSee you next time...")
    sys.exit()


if user_input == 1:

    user_input = int(input('\n1.4 AM\n2.10 AM\n3.4 PM \n\n>'))
    
    if user_input == 1:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '4'
    elif user_input == 2:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '9'
    elif user_input == 3:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '16'

    main_user_date = user_select_date
    main_user_time = user_time

    program_successful = route_report_download.download_report(user_select_date, user_select_time)
    # program_successful = True

    if program_successful:
        print("\nDownload was Successfull!")
        user_input = int(input("\nIs the report inside the download folder?\n1.Yes, Continue...\n2.Download Manually\n\n>"))

        path_to_file = glob.glob( str(Path.cwd().parents[0]) + '/Route+report' + '*.xlsx')

        if os.path.exists(path_to_file[0]):
            os.replace(path_to_file[0], str(Path.cwd()) + '/INPUT/client_report.xlsx')
        else:
            print("\n\nPlease add file inside the INPUT folder as client_report.xlsx")
            exit()
        
        if user_input == 1:

            user_input = int(input("\nConvert Report?\n1.Yes\n2.No\n\n>"))
            if user_input == 1:
                program_successful = route_report_convert.convert_report(user_select_date, user_select_time)
                # program_successful = True

                if program_successful:

                    print("\nConversion done Please check the output folder and verify if everything is fine and add ALARMS file in there too...\n")

                    user_input = int(input("\nIs the alarms.xlsx file in the folder??\n1.Yes\n2.No\n\n>"))
                    if user_input == 1:
                            program_successful = route_report_alarms.add_alarms(user_select_date, user_select_time)
                            # program_successful = True

                            if program_successful:

                                print("\n\n\nAlarms added to the Route report successfully, please verify report before the next step!!!")

                                user_input = int(input("\nIs the report veryfied and ready to send to client?\n1.Yes, Continue...\n2.No\n\n>"))
                                if user_input == 1:

                                    user_input = int(input("\nSend Report To Client?\n1.Yes\n2.No\n\n>"))
                                    if user_input == 1:
                                        program_successful = route_report_mail.send_mail(user_select_date, user_select_time)
                                        # program_successful = True

                                        if program_successful:
                                            print("\n\n\nReport was sent to client successfully\nHave a wonderfull day!!!")
                                        else:
                                            print("\n\nERROR - Something went wrong please check the reportLOGS.txt file")
                                            exit()
                                    else:
                                        print("\n\nCome back when you need me...!!\n") 
                                        exit()
                                else:
                                    print("\n\nCome back when you need me...!!\n") 
                                    exit()
                            else:
                                print("\n\nERROR - Something went wrong please check the reportLOGS.txt file")
                                exit()
                    else:
                        print("\n\nPlease add the alarms file then come back we finish this work...!!\n") 
                        exit()
                else:
                    print("\n\nERROR - Something went wrong please check the reportLOGS.txt file")
                    exit()
            else:
                print("\n\nCome back when you need me...!!\n") 
                exit()
        else:
            print("\n\nPlease Download the report and rerun the script...!!\n") 
            exit()
    else:
        print("\n\nERROR - Something went wrong please check the reportLOGS.txt file")
        exit()
    
elif user_input == 2:

    user_input = int(input('\n1.4 AM\n2.9 AM\n3.4 PM \n\n>'))

    if user_input == 1:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '4'
    elif user_input == 2:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '9'
    elif user_input == 3:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '16'
    
    program_successful = route_report_convert.convert_report(user_select_date, user_select_time)

    if program_successful:
        print("\nReport was converted successfully\nPlease check the output folder!!!")
    else:
        print("\nERROR - Something went wrong please check the reportLOGS.txt file")
        exit()

elif user_input == 3:

    user_input = int(input('\n1.4 AM\n2.9 AM\n3.4 PM \n\n>'))

    if user_input == 1:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '4'
    elif user_input == 2:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '9'
    elif user_input == 3:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '16'

    program_successful = route_report_alarms.add_alarms(user_select_date, user_select_time)

    if program_successful:
        print("\nAlarms added to the Route report successfully, please verify report before the next step!!!\n\n")
    else:
        print("\nERROR - Something went wrong please check the reportLOGS.txt file")
        exit()

elif user_input == 4:

    user_input = int(input('\n1.4 AM\n2.9 AM\n3.4 PM \n\n>'))
    
    if user_input == 1:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '4'
    elif user_input == 2:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '9'
    elif user_input == 3:
        user_select_date = str(datetime.now().strftime("%d")).lstrip("0")
        user_select_time = '16'
    
    program_successful = route_report_mail.send_mail(user_select_date, user_select_time)

    if program_successful:
        print("\nReport was sent to client successfully\nHave a wonderfull day!!!")
    else:
        print("\nERROR - Something went wrong please check the reportLOGS.txt file")
        exit()