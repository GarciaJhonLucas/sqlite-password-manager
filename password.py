from Conexion import *

def register(name, url, user_name, user_pass, description):
    try:
        conexion = conection()
        cursor = conexion.cursor()
        sql = '''INSERT INTO passwords (name, url, user_name, user_pass, description) 
        VALUES (?, ?, ?, ?, ?)'''
        data = (name, url, user_name, user_pass, description)
        cursor.execute(sql, data)
        conexion.commit()
        conexion.close()
        return 'Correct'
    except Error as err:
        return 'An error has occurred '+str(err)

def show_all():
    data = []
    try:
        conexion = conection()
        cursor = conexion.cursor()
        sql = 'SELECT * FROM passwords'
        cursor.execute(sql)
        data = cursor.fetchall()
        conexion.close()
    except Error as err:
        return 'An error has occurred '+str(err)
    return data

def find_pass(id):
    data = []
    try:
        conexion = conection()
        cursor = conexion.cursor()
        sql = 'SELECT * FROM passwords WHERE id = ?'
        cursor.execute(sql, (id,))
        data = cursor.fetchall()
        conexion.close()
    except Error as err:
        return 'An error has occurred '+str(err)
    return data

def modify(id, name, url, user_name, user_pass, description):
    try:
        conexion = conection()
        cursor = conexion.cursor()
        sql = 'UPDATE passwords SET name = ?, url = ?, user_name = ?, user_pass = ?, description = ? WHERE id = ?'
        data = (name, url, user_name, user_pass, description, id)
        cursor.execute(sql, data)
        conexion.commit()
        conexion.close()
        return 'It was successfully modified'
    except Error as err:
        return 'An error has occurred '+str(err)

def delete(id):
    try:
        conexion = conection()
        cursor = conexion.cursor()
        sql = 'DELETE FROM passwords WHERE id = ?'
        cursor.execute(sql, (id))
        conexion.commit()
        conexion.close()
        return 'It was successfully deleted'
    except Error as err:
        return 'An error has occurred '+str(err)
