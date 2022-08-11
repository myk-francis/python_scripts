import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="myk",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="betsavage")
    cursor = connection.cursor()
    print("Connection to DATABASE was established!\n")

    # creating a cursor
    cursor = connection.cursor()
    
    # list of rows to be inserted
    
    # values = [  
    #     ('Arsenal', 'ARS', 1, 1, 0, 0, 2, 2, 0, 2, 1, 3), 
    #     ('Aston Villa', 'AVL', 1, 0, 1, 0, 2, 2, 0, 16, 1, 0),
    #     ('Bournemouth', 'BOU', 1, 1, 0, 0, 2, 2, 0, 3, 1, 3),
    #     ('Brentford', 'BRE', 1, 0, 0, 1, 2, 2, 0, 9, 1, 1),
    #     ('Brighton & Hove Albion', 'BRI', 1, 1, 0, 2, 2, 0, 0, 6, 1, 3),
    #     ('Chelsea', 'CHE', 1, 1, 0, 0, 1, 1, 0, 8, 1, 3),
    #     ('Crystal Palace ', 'CRY', 1, 0, 1, 0, 2, 2, 0, 17, 1, 0),
    #     ('Fulham', 'FUL', 1, 0, 0, 1, 4, 2, 2, 10, 1, 1),
    #     ('Everton', 'EVE', 1, 0, 0, 1, 1, 1, 0, 15, 1, 0),
    #     ('Leeds United', 'LEE', 1, 1, 0, 0, 3, 2, 1, 7, 1, 3),
    #     ('Leicester City', 'LEI', 1, 0, 0, 1, 4, 2, 2, 11, 1, 1),
    #     ('Liverpool', 'LIV', 1, 0, 0, 1, 4, 2, 2, 12, 1, 1),
    #     ('Manchester City ', 'MCI', 1, 1, 0, 0, 2, 2, 0, 4, 1, 3),
    #     ('Manchester United ', 'MUN', 1, 0, 1, 0, 3, 2, 1, 13, 1, 0),
    #     ('Newcastle United', 'NEW', 1, 1, 0, 0, 2, 2, 0, 5, 1, 3),
    #     ('Nottingham Forest', 'FOR', 1, 0, 1, 0, 0, 2, 0, 18, 1, 0),
    #     ('Southampton', 'SOT', 1, 0, 1, 0, 5, 3, 2, 20, 1, 0),
    #     ('Tottenham Hotspur ', 'TOT', 1, 1, 0, 0, 5, 3, 3, 1, 1, 3),
    #     ('West Ham United ', 'WHU', 1, 0, 1, 0, 2, 2, 0, 19, 1, 0),
    #     ('Wolverhampton Wanderers', 'WOL', 1, 0, 1, 0, 3, 2, 1, 14, 1, 0),
    # ]
    
    # cursor.mogrify() to insert multiple values
    args = ','.join(cursor.mogrify("(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", i).decode('utf-8')
                    for i in values)
    
    # executing the sql statement
    cursor.execute("INSERT INTO teams(name, code, played, wins, loses, draws, goals, first_half_goals, sec_half_goals, rank, season, points) VALUES " + (args))
    
    # select statement to display output
    sql1 = '''SELECT * FROM teams;'''
    
    # executing sql statement
    cursor.execute(sql1)
    
    # fetching rows
    for i in cursor.fetchall():
        print(i)
    
    # commiting changes
    connection.commit()

    count = cursor.rowcount
    print(count, "Record inserted successfully into teams table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into teams table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")