import os 
from getpass import getpass
from tabulate import tabulate
from Conexion import *
import user
import password

conexion = conection()
create_table(conexion)

def start():
    os.system('cls')
    check = user.check_user()
    if len(check) == 0:
        print('Welcome Enter a new user')
        name = input('Enter your name: ')
        last_name = input('Enter your last name: ')
        pass_key = getpass('Enter your pass key: ')
        result = user.register_user(name, last_name, pass_key)
        if result == 'Correct':
            print(f'Welcome {name}')
            menu()
        else:
            print(result)
    else:
        pass_key = getpass('Enter your admin pass : ')
        result = user.check_pass(1, pass_key)
        if len(result) == 0:
            print('Password Incorrect')
        else:
            print('Welcome')
            menu()

def menu():
    while True:
        print('Choose and option')
        print('\t 1- Add password')
        print('\t 2- Show passwords')
        print('\t 3- Show a password')
        print('\t 4- Modify a password')
        print('\t 5- Delete a password')
        print('\t 6- Exit')
        option = input('Enter an option: ')

        if option == '1':
            new_pass()
        elif option == '2':
            show_pass()
        elif option == '3':
            find_pass()
        elif option == '4':
            modify_pass()
        elif option == '5':
            delete_pass()
        elif option == '6':
            break
        else:
            print("No ingreso un rreueta valida")

def new_pass():
    name = input('Enter the name: ')
    url = input('Enter the url: ')
    user_name = input('Enter the user name: ')
    user_pass = getpass('Enter the user pass: ')
    description = input('Enter the description: ')
    result = password.register(name, url, user_name, user_pass, description)
    print(result)

def show_pass():
    data = password.show_all()
    new_data = []
    header = ['ID', 'NAME', 'URL', 'USER', 'PASSWORD', 'DESCRIPTION']
    for d in data:
        convert = list(d)
        convert[4] = '*********'
        new_data.append(convert)

    table = tabulate(new_data, header, tablefmt = 'fancy_grid')
    print('\t\t All passwords')
    print(table)

def find_pass():
    pass_key = getpass('Enter your admin pass: ')
    result = user.check_pass(1, pass_key)
    if (len(result)) == 0:
        print("Stop you aren't admin")
    else:
        id = input('Enter the id of the password: ')
        data = password.find_pass(id)
        header = ['ID', 'NAME', 'URL', 'USER', 'PASSWORD', 'DESCRIPTION']
        table = tabulate(data, header, tablefmt = 'fancy_grid')
        print('\t\t All passwords')
        print(table)

def modify_pass():
    pass_key = getpass('Enter your admin pass: ')
    result = user.check_pass(1, pass_key)
    if (len(result)) == 0:
        print("Stop you aren't admin")
    else:
        id = input('Enter the id of the password: ')
        name = input('Enter the new name: ')
        url = input('Enter the new url: ')
        user_name = input('Enter the new user name: ')
        user_pass = getpass('Enter the new user pass: ')
        description = input('Enter the new description: ')
        result = password.modify(id, name, url, user_name, user_pass, description)
        print(result)

def delete_pass():
    pass_key = getpass('Enter your admin pass: ')
    result = user.check_pass(1, pass_key)
    if (len(result)) == 0:
        print("Stop you aren't admin")
    else:
        id = input('Enter the id of the password to delete: ')
        result = password.delete(id)
        print(result)


start()