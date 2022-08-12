import psycopg2
import openpyxl
from pathlib import Path

try:
    connection = psycopg2.connect(user="postgres",
                                  password="myk",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="test_db")
    cursor = connection.cursor()
    print("Connection to DATABASE was established!\n")
    print("Reading Manifest Report...\n\n")

    #creating a cursor
    cursor = connection.cursor()

    route_data = []

    
    client_wb = openpyxl.load_workbook(f'{str(Path.cwd())}/INPUT/manifest.xlsx')
    client_sheet = client_wb.active

    for row in range(2, 1000):

        row_data = []

        for col in range(3, 17):
            row_data.append(client_sheet.cell(row=row, column=col).value)
                    
        if all(i is None for i in row_data):
            break

        # del row_data[8:10]
        row_data.pop(8)
        row_data.pop(11)
        
        for j in range(len(row_data)):
            if (row_data[j] == None) and (j != 8) and (j != 10)and (j != 11):
                row_data[j] = ''

        #Ordering the list
        myorder = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11]
        duplicate_list_data = []
        for i in myorder:
            order_data = row_data[i] 
            duplicate_list_data.append(order_data)
        
                
        route_data.append(tuple(duplicate_list_data))

    
    # list of rows to be inserted
    # cursor.mogrify() to insert multiple values
    args = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", i).decode('utf-8')
                    for i in route_data)
    
    # executing the sql statement
    cursor.execute("INSERT INTO manifest (device_id , cargo_type, load_point, destination, country, transporter,  horse, trailer_1 , trailer_2, tag_request_date, tag_installation_date, trip_end_time) VALUES " + (args))
    
    # commiting changes
    connection.commit()

    print("Record inserted successfully into manifest table...\n\n")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into manifest table\n\n", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed\n\n")