import hashlib
from Conexion import *

def check_user():
    conexion = conection()
    cursor = conexion.cursor()
    sql = 'SELECT * FROM users'
    cursor.execute(sql)
    user_found = cursor.fetchall()
    conexion.close()
    return user_found

def register_user(name, last_name, pass_key):
    try:
        conexion = conection()
        cursor = conexion.cursor()
        sql = '''INSERT INTO users 
        (name, last_name, pass_key)
        values(?, ?, ?)'''
        cm_encrypted = hashlib.sha256(pass_key.encode('utf-8')).hexdigest()
        data = (name, last_name, cm_encrypted)
        cursor.execute(sql, data)
        conexion.commit()
        conexion.close()
        return 'Correct'
    except Error as err:
        return 'An error has occurred '+str(err)

def check_pass(id, pass_key):
    try:
        conexion = conection()
        cursor = conexion.cursor()
        sql = 'SELECT * FROM users WHERE id = ? AND pass_key = ?'
        cm_encrypted = hashlib.sha256(pass_key.encode('utf-8')).hexdigest()
        cursor.execute(sql, (id, cm_encrypted))
        data = cursor.fetchall()
        cursor.close()
        return data
    except Error as err:
        return 'An error has occurred '+str(err)
