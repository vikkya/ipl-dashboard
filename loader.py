import sqlite3
from sqlite3 import Error
import csv


class Loader():
    def create_connection(self,db_file):
        ####
        # Create a database connection
        ####
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as err:
            print(err)

        return conn

    def create_table(self,conn, table_name, columns):
        #############
        # Create a table into db 
        # Parameters connection string, table name, and column names with data type in string format
        ##############
        cols = columns.replace('"', '')
        sql = f'create table if not exists {table_name}({cols})'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()


    def insert(self,conn,table_name, record):
        ############
        # Inserts into table with the records as tuple
        ############
        sql = f""" insert into {table_name}(id, city, date, player_of_match, venue, neutral_venue, team1, team2, toss_winner, toss_decision, winner, result, result_margin, eliminator, method, umpire1, umpire2) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """
        cur = conn.cursor()
        cur.execute(sql, record)
        conn.commit()
        return cur.lastrowid


    def main(self):
        db = "xyz.db"
        conn = self.create_connection(db)
        self.create_table(conn,"match","id real, city text, date date, player_of_match text, venue text, neutral_venue text, team1 text, team2 text, toss_winner text, toss_decision text, winner text, result text, result_margin real, eliminator text, method text, umpire1 text, umpire2 text")
        with conn:
            with open("ipldata.csv", "r") as f:
                csv_content = csv.DictReader(f)
                for i in csv_content:
                    print(tuple(i.values()))
                    self.insert(conn, "match", tuple(i.values()))
        conn.close()
