#!/usr/bin/env python3

import sqlite3
import csv
from pathlib import Path

class DB:
    
    def __init__(self, db_file: str):

        self.db_file = db_file
        self.con = self.create_connection()
        self.cur = self.con.cursor()

    def create_connection(self) -> sqlite3.Connection:
        '''Creates the connection to the database.
           If the database doesn't exists, the method creates one.'''

        try:
            con: sqlite3.Connection = sqlite3.connect(self.db_file, check_same_thread=False)
        except Exception as e:
            print(f"{e}\n Connection to database hasn't been established.")

        return con

    def create_table(self, table_name: str, **kwargs) -> None:
        ''' Creates the table. Receives the table name and the column names assigned
            with their datatype.
            For example: create_table('Spam', id='text', salary='real' . . .)
        '''

        correct_datatypes: list[str] = ["INTEGER", "REAL", "NUMERIC", "TEXT", "BLOB"]
        columns:           list[str] = [f"{key} {value}" for key, value 
                                    in kwargs.items() 
                                    if value.upper() in correct_datatypes]
        
        assert len(kwargs) == len(columns), "Not permited datatypes has been used."
        
        if not self.cur.execute(f'CREATE TABLE {table_name}({", ".join(columns)});'):
            raise Exception('Creation of table has failed. Check you parameters.')

        self.con.commit()


    def add_to_table(self, table_name, **columns, ) -> None:
        ''' Receives the name of the target table, then a series of the target columns
            assigned with the desired value.
        '''
        
        column_names:    str = ", ".join(list(columns.keys())) 
        column_values: tuple = tuple(columns.values())
        place_holders:   str = ", ".join(['?' for _ in columns])
        cmd: str = f'INSERT INTO {table_name}({column_names}) VALUES ({place_holders});'
        
        self.cur.executemany(cmd, (column_values, ))
        
        self.con.commit()

    
    def fetch_table_from_csv(self, source: str, table_name: str,  **kwargs) -> None: 
        ''' Alternative for db creation from csv. Receives the route of the .csv file as "source",
            then the desired table_name, and the columns assigned with their datatype.
        '''
       
        table_defs: str = ", ".join([f'{key} {value}' for key, value in kwargs.items()])
        self.cur.execute(f'CREATE TABLE {table_name}({table_defs});')

        with open(source, 'r') as x: 
            content = csv.reader(x, delimiter=';') 

            data_set: list[tuple] = [tuple(i) for i in list(content)] 
        
            column_names:  str = ", ".join(list(data_set[0])) 
            place_holders: str = ", ".join(['?' for _ in data_set[1]])
            cmd:           str = f'INSERT INTO {table_name}({column_names}) VALUES ({place_holders});'

        self.cur.executemany(f'INSERT INTO {table_name}({column_names}) VALUES ({place_holders});', data_set)
        self.con.commit()


    def get_query(self, column: str, search_term: str) -> list[tuple]:
        ''' Get's as args the "to be queried" column name, and the search term where the
            one of the column value supposed to be similar.
        '''
                                                    # Makes title and search_term uppercase to be case insensitive.
        self.cur.execute(f"SELECT {column} FROM animes WHERE upper(title) LIKE ?", (f"%{search_term.upper()}%", ))

        registers: list[tuple] = self.cur.fetchall()

        return registers


    def model_result(self, registers: list[tuple]) -> list[str]:
        ''' "model_result" basically is a pretty print. Splits the query result into 
            determined size of line chunks, then returns it as a list of "paragraphs".
        '''

        modeled_output: list[str] = []

        for row in registers:
            word_list: list[str] = "".join(list(row)).split(' ') 
            paragraph: str = " ".join([" ".join(word_list[i:i+8]) for i in range(0,len(word_list),8)])
            modeled_output.append(paragraph)
        
        return modeled_output

if __name__ == "__main__":
    ''' Only for the first time to be executed to build the database
        for the Flask web app . . . 
    '''

    anime: DB = DB('./db_src/source.db')
#     anime.create_table('animes', id='integer', title='text', desc='text')
#     anime.add_to_table('animes', id='1', title='test', desc='test')
#     test: list[tuple] = anime.get_query('select desc from animes;',())
#     a = anime.model_result(test)
    anime.fetch_table_from_csv('db_src/animes_src.csv', 
                               'animes', 
                               id='integer',
                               title='text',
                               desc='text')

