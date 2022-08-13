import manifest_db
import route_report_db
import alarms_db

user_input = int(input('1.Upload Manifest\n2.Upload Route Report\n3.Upload Alarms\n4.Quit\n\n>'))

if (user_input != 1) or (user_input != 1) or (user_input != 1):
    print('Have a nice day :)')
    exit()

if user_input == 1:
    manifest_db.upload_manifest()
elif user_input == 2:
    route_report_db.upload_report()
elif user_input == 3:
    alarms_db.upload_alarms()



