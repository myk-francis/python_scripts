import psycopg2
import pandas as pd
import pandas.io.sql as psql

def insert_to_table(home_team, away_team, home_goals, away_goals, first_half_goals, sec_half_goals, total_goals, match_result, bet_value, over_under, win_lose, round):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="myk",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="betsavage")

        cursor = connection.cursor()

        print("DATABASE connected successfully!!!\n\n")

        insert_query = """ INSERT INTO games (
        home, 
        away, 
        home_goals, 
        away_goals, 
        first_half_goals, 
        sec_half_goals, 
        total_goals, 
        match_result, 
        bet_value, 
        over_under, 
        bet_win_lose,
        round
        ) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (home_team, away_team, home_goals, away_goals, first_half_goals, sec_half_goals, total_goals, match_result, bet_value, over_under, win_lose, round)
        cursor.execute(insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into games table\n\n")

        games= psql.read_sql("SELECT * FROM games", connection)
        print(games)
        print("\n\n")

    except (Exception, psycopg2.Error) as error:
        print("Error in Inserting operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def update_table(home_team, away_team, home_goals, away_goals, first_half_goals, sec_half_goals, total_goals, match_result, bet_value, over_under, win_lose):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="myk",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="betsavage")

        cursor = connection.cursor()

        print("Updating teams table!!!\n\n")
        teams= psql.read_sql("SELECT * FROM teams ORDER BY id ASC", connection)
        print(teams)
        print("\n\n")


        print("Table Before updating record \n\n")
        sql_select_query = """SELECT * FROM teams WHERE code = (%s)"""
        cursor.execute(sql_select_query, (home_team,))
        home_record = cursor.fetchone()

        played = home_record[3] + 1

        if match_result == home_team:
            wins = home_record[4] + 1
            loses = home_record[5]
            draws = home_record[6]
            home_points = home_record[12] + 3

        elif match_result == "Draw":
            draws = home_record[6] + 1
            home_points = home_record[12] + 1
            wins = home_record[4]
            loses = home_record[5]

        else:
            loses = home_record[5] + 1
            wins = home_record[4]
            draws = home_record[6]
            home_points = home_record[12] 

        goals = home_record[7] + total_goals

        home_first_half_goals = home_record[8] + first_half_goals

        home_sec_half_goals = home_record[9] + sec_half_goals
        

        # Update single record now HOME team
        sql_update_query = """UPDATE teams SET 
                                played = %s,
                                wins = %s,
                                loses = %s,
                                draws = %s,
                                goals = %s,
                                first_half_goals = %s,
                                sec_half_goals = %s,
                                points = %s
                            WHERE code = %s"""
        cursor.execute(sql_update_query, (played, wins, loses, draws, goals, home_first_half_goals, home_sec_half_goals, home_points, home_team))
        connection.commit()

        sql_select_query = """SELECT * FROM teams WHERE code = (%s)"""
        cursor.execute(sql_select_query, (away_team,))
        away_record = cursor.fetchone()

        played = away_record[3] + 1

        if match_result == away_team:
            wins = away_record[4] + 1
            loses = away_record[5]
            draws = away_record[6]
            away_points = away_record[12] + 3

        elif match_result == "Draw":
            draws = away_record[6] + 1
            away_points = away_record[12] + 1
            wins = home_record[4]
            loses = home_record[5]

        else:
            loses = away_record[5] + 1
            wins = away_record[4]
            draws = away_record[6]
            away_points = away_record[12] 

    
        goals = away_record[7] + total_goals

        away_first_half_goals = away_record[8] + first_half_goals

        away_sec_half_goals = away_record[9] + sec_half_goals
        

        # Update single record now AWAY team
        sql_update_query = """UPDATE teams SET 
                                played = %s,
                                wins = %s,
                                loses = %s,
                                draws = %s,
                                goals = %s,
                                first_half_goals = %s,
                                sec_half_goals = %s,
                                points = %s
                            WHERE code = %s"""
        cursor.execute(sql_update_query, (played, wins, loses, draws, goals, away_first_half_goals, away_sec_half_goals, away_points, away_team))
        connection.commit()
        
        print("Records Updated successfully\n\n")

        print("After updating teams table!!!\n\n")
        teams= psql.read_sql("SELECT * FROM teams ORDER BY id DESC", connection)
        print(teams)
        print("\n\n")

    except (Exception, psycopg2.Error) as error:
        print("Error in Updating operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")



try:
    connection = psycopg2.connect(user="postgres",
                                      password="myk",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="betsavage")

    cursor = connection.cursor()

    print("Lets Get it!!!\n\n")

    teams = pd.read_sql('SELECT * FROM teams ORDER BY id DESC', connection)
    print(teams)
    print("\n\n")

    round = int(input("\nRound?\n>"))

    home_team = input("Home team:")

    away_team = input("\nAway team:")

    match_result = str(input("\nMatch result: \n1.Home Win\n2.Away Win\n3.Draw\n>"))

    total_goals = int(input("\nTotal Goals:"))

    bet_input = input("\nDid you put up a parley?\n1.Yes\n2.No\n>")

    if bet_input == '1':
        bet_value = input("\nWhat was it:")

        over_under = str(input("\n1.Over\n2.Under\n>"))
        if over_under == '1':
            over_under = "over"
        else:
            over_under = "under"

        win_lose = str(input("\n1.Won\n2.Lost\n>"))
        if win_lose == '1':
            win_lose = "won"
        else:
            win_lose = "lost"
    else:
        bet_value = ""
        over_under = ""
        win_lose = ""

    if match_result == '1':
        match_result = home_team
    elif match_result == '2':
        match_result = away_team
    else:
        match_result = "Draw"

    if total_goals > 0:
        first_half_goals = int(input("\nFirst Half Goals:"))
        sec_half_goals = int(input("\nSecond Half Goals:"))

        home_goals = int(input("\nHome Goals:"))
        away_goals = int(input("\nAway Goals:"))
    else:
        first_half_goals = 0
        sec_half_goals = 0

        home_goals = 0
        away_goals = 0

    insert_to_table(home_team, away_team, home_goals, away_goals, first_half_goals, sec_half_goals, total_goals, match_result, bet_value, over_under, win_lose, round)

    update_table(home_team, away_team, home_goals, away_goals, first_half_goals, sec_half_goals, total_goals, match_result, bet_value, over_under, win_lose)

    print("\n\n\n***************     PROGRAM END     *****************************\n\n\n")

except (Exception) as error:
    print("Something went wrong with the main program\n\n", error)


finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("\nPostgreSQL connection is closed\n")
        print("Program End...!!!\n\n")