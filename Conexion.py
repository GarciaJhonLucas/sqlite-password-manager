import sqlite3
from sqlite3 import *

def conection():
    try:
        conexion = sqlite3.connect('database.db')
        return conexion
    except Error as err:
        print('Error')

def create_table(conexion):
    cursor = conexion.cursor();
    sql_user = '''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        last_name TEXT NOT NULL, 
        pass_key TEXT NOT NULL 
    )'''
    sql_pass = ''' CREATE TABLE IF NOT EXISTS passwords(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        url TEXT NOT NULL, 
        user_name TEXT NOT NULL, 
        user_pass TEXT NOT NULL, 
        description TEXT
    ) '''
    cursor.execute(sql_user)
    cursor.execute(sql_pass)
    conexion.commit()
