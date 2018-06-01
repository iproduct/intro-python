import sqlite3, os

def get_db():
    DATABASE = os.path.join('.', 'blog.sqlite')
    db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    f = open('schema.sql', 'r')
    #print(f.read())
    db.executescript(f.read())

def insert_user(username, password):
    db.execute('INSERT INTO user (username, password) VALUES (?, ?)',
               (username, password))
    db.commit()

def get_all_users():
    users = db.execute('SELECT * FROM user').fetchall()
    return users

def print_users(user_list):
    for user in user_list:
        print ('ID: ', user['id'],', username: ', user['username'], ', password: ', user['password'])

db = get_db()

if __name__ == "__main__":
    init_db()
    insert_user("ivan", "ivan567")
    insert_user("petar", "pythonisfun")
    insert_user("dimitar", "hero123")
    user_list = get_all_users()
    print_users(user_list)
    db.close();
    print('DB closed ...')
