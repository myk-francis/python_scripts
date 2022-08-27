import psycopg2
import pandas as pd
import pandas.io.sql as psql

def predict_result():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="myk",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="betsavage")

        cursor = connection.cursor()

        teams = pd.read_sql('SELECT * FROM teams ORDER BY points DESC', connection)
        print(teams)
        print("\n\n")

        home_team = input('\nHome Team:')

        away_team = input('\n\nAway Team:')

        cursor.execute("SELECT name FROM teams WHERE code = %s", (home_team,))

        if cursor.fetchone() == None:
            print(f'Home Team Code: {home_team} does not exist. Please check the below options...\n\n\n')
            print(pd.read_sql('SELECT home, code FROM teams ORDER BY id DESC', connection))
            exit()

        cursor.execute("SELECT name FROM teams WHERE code = %s", (away_team,))

        if cursor.fetchone() == None:
            print(f'Away Team Code: {away_team} does not exist. Please check the below options...\n\n\n')
            print(pd.read_sql('SELECT home, code FROM teams ORDER BY id DESC', connection))
            exit()

        cursor.execute("SELECT SUM(total_goals) AS sum_goals FROM games WHERE home IN (%s, %s) OR away IN (%s, %s)", (home_team, away_team,home_team, away_team,))

        result_goals = cursor.fetchone()

        team_goals = int(result_goals[0])

        cursor.execute("SELECT count(*) AS count_rows FROM games WHERE home IN (%s, %s) OR away IN (%s, %s)", (home_team, away_team,home_team, away_team,))

        result_rows = cursor.fetchone()

        match_count = int(result_rows[0])

        average_goals = round(team_goals / match_count, 2)

        margin_of_error = round(team_goals / match_count, 2) - 1

        print(f'\n\nTEAM GOALS: {team_goals}\n')

        print(f'\n\nNUMBER OF GAMES: {match_count}\n')

        print(f'\n\nAVERAGE GOALS: {average_goals}\n')

        print(f'\n\nMARGIN OF ERROR IN GOALS: {margin_of_error}\n')

        if margin_of_error > 2:
            print('\n\nOVER 1.5 FOR THIS')
        else:
            print('\n\nUNDER 3.5 FOR THIS')

        exit()

    except Exception as error:
        print("\n\nError in Predicting Match", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("\n\nPostgreSQL connection is closed") 

predict_result()