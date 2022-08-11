
import psycopg2 
import pandas as pd
import pandas.io.sql as psql

connection = psycopg2.connect(user="postgres",
                                      password="myk",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="betsavage")

cursor = connection.cursor()



print("Table Before updating record \n\n")
sql_select_query = """SELECT * FROM teams WHERE code IN (%s,%s)"""
cursor.execute(sql_select_query, ('FUL', 'ARS'))
record = cursor.fetchall()
print(record)

if connection:
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")