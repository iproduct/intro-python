from flask import Flask, render_template, g, request, redirect
import sqlite3

DATABASE = './blog.sqlite'
app = Flask(__name__)


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row
    return g.db


def get_all_users():
    users = g.db.execute('SELECT * FROM user').fetchall()
    return users


def print_users(user_list):
    for user in user_list:
        print('ID: ', user['id'], ', username: ', user['username'], ', password: ', user['password'])


@app.route('/users/add', methods=('GET', 'POST'))
def add_user():
    g.active_url = '/users/add'
    error=None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {0} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, password)
            )
            db.commit()
            return redirect('/users')

    return render_template('user/add-user.html', error=error)

@app.route('/users')
def users():
    g.active_url = '/users'
    db = get_db()
    users = get_all_users()
    print_users(users)
    return render_template('user/users.html', users=users)


@app.route('/')
def home():
    g.active_url = '/'
    return render_template('home/home.html')


if __name__ == '__main__':
    app.run()
