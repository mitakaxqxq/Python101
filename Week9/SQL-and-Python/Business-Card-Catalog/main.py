import sqlite3


def print_user_details(user):
    print('###############')
    print(f'Id: {user[0]}')
    print(f'Full name: {user[1]}')
    print(f'Email: {user[2]}')
    print(f'Age: {user[3]}')
    print(f'Phone: {user[4]}')
    print(f'Additional info: {user[5]}')
    print('###############')


def create_user_table():
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            full_name VARCHAR(255) NOT NULL,
            email VARCHAR(100) NOT NULL,
            age INTEGER NOT NULL,
            phone VARCHAR(15) NOT NULL,
            additional_info TEXT
        )
        ''')

    connection.commit()
    connection.close()


def help():
    print('#############\n###Options###\n#############')
    print('1. `add` - insert new business card')
    print('2. `list` - list all business cards')
    print('3. `delete` - delete a certain business card (`ID` is required)')
    print('4. `get` - display full information for a certain business card (`ID` is required)')
    print('5. `help` - list all available options')


def add():
    full_name = input('Enter user name: ')
    email = input('Enter email: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    additional_info = input('Enter addional info (optional): ')

    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()
    insert_query = f'''
    INSERT INTO User (full_name, email, age, phone, additional_info) VALUES (?, ?, ?, ?, ?)
    '''

    cursor.execute(insert_query, (full_name, email, age, phone, additional_info))
    connection.commit()
    connection.close()


def list_users():
    print('#############\n###Contacts###\n#############')
    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()

    select_query = f'''
    SELECT id, email, full_name FROM User
    '''
    cursor.execute(select_query)
    list_of_users = cursor.fetchall()

    for number, user in enumerate(list_of_users):
        print(f'{number+1}. ID: {user[0]}, Email: {user[1]}, Full name: {user[2]}')

    connection.commit()
    connection.close()


def get():
    user_id = input('Enter id: ')

    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()

    select_query = f'''
    SELECT * FROM User WHERE id = {user_id}
    '''

    cursor.execute(select_query)
    user = cursor.fetchone()

    if user is None:
        print(f'No user was found with id = {user_id}.')
    else:
        print('\nContact info:\n')
        print_user_details(user)

    connection.commit()
    connection.close()


def delete():
    user_id = input('Enter id: ')

    connection = sqlite3.connect('business_cards.db')
    cursor = connection.cursor()

    select_query = f'''
    SELECT * FROM User WHERE id = {user_id}
    '''

    cursor.execute(select_query)
    user = cursor.fetchone()

    if user is None:
        print(f'No user was found with id = {user_id}.')
    else:
        print('\nFollowing contact is deleted successfully:\n')
        print_user_details(user)

    delete_query = f'''
    DELETE FROM User WHERE id == {user_id}
    '''

    cursor.execute(delete_query)
    connection.commit()
    connection.close()


def main():
    create_user_table()
    print(
        'Hello! This is your business card catalog. What would you like? (enter "help" to list all available options)'
    )

    while True:
        command = input('>>> Enter command: ')
        if command == 'help':
            help()
        elif command == 'add':
            add()
        elif command == 'list':
            list_users()
        elif command == 'get':
            get()
        elif command == 'delete':
            delete()
        else:
            print('Invalid command - try again!')


if __name__ == '__main__':
    main()
