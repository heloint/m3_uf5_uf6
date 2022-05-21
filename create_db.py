#!/usr/bin/env python3

import sqlite3
import csv
from pathlib import Path

class DB:
    

    def __init__(self, db_file: str):

        self.db_file = db_file
        self.con = self.create_connection()
        self.cur = self.con.cursor()

    def create_connection(self):
        
        con = None

        try:
            con = sqlite3.connect(self.db_file)
        except Exception as e:
            print(f"{e}\n Connection to database hasn't been established.")

        return con

    def create_table(self, table_name: str, **kwargs):


        correct_datatypes = ["INTEGER", "REAL", "NUMERIC", "TEXT", "BLOB"]
        columns = [f"{key} {value}" for key, value 
                                    in kwargs.items() 
                                    if value.upper() in correct_datatypes]
        
        assert len(kwargs) == len(columns), "Not permited datatypes has been used."
        
        if not self.cur.execute(f'CREATE TABLE {table_name}({", ".join(columns)});'):
            raise Exception('Creation of table has failed. Check you parameters.')

        self.con.commit()


    def add_to_table(self, table_name, **columns, ):
        
        
        column_names: str = ", ".join(list(columns.keys())) 
        column_values: str = tuple(columns.values())
        place_holders: list[str] = ", ".join(['?' for _ in columns])
        cmd: str = f'INSERT INTO {table_name}({column_names}) VALUES ({place_holders});'
        
        self.cur.executemany(cmd, (column_values, ))
        
        self.con.commit()

    
    def fetch_table_from_csv(self, source: str, table_name: str,  **kwargs) -> None: 

       
        table_defs: str = ", ".join([f'{key} {value}' for key, value in kwargs.items()])
        self.cur.execute(f'CREATE TABLE {table_name}({table_defs});')


        with open(source, 'r') as x: 
            content = csv.reader(x, delimiter=';') 

            data_set = [tuple(i) for i in list(content)] 
        
            column_names: str = ", ".join(list(data_set[0])) 
            place_holders: str = ", ".join(['?' for _ in data_set[1]])
            cmd: str = f'INSERT INTO {table_name}({column_names}) VALUES ({place_holders});'

        self.cur.executemany(f'INSERT INTO {table_name}({column_names}) VALUES ({place_holders});', data_set)
        
        self.con.commit()

anime = DB('source.db')
# anime.create_table('animes', id='integer', title='text', desc='text')
# anime.add_to_table('animes', id='1', title='test', desc='test')
# anime.fetch_table_from_csv('test.csv', 
#                            'animes', 
#                            id='integer',
#                            title='text',
#                            desc='text')

