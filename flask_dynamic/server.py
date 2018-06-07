from flask import Flask, render_template, g, request, redirect, url_for, session, flash
import sqlite3

DATABASE = './blog.sqlite'
app = Flask(__name__)
app.secret_key = 'any random string'


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

def print_user(user):
    print('ID: ', user['id'], ', username: ', user['username'], ', password: ', user['password'],
              ', role: ', user['role'])

def print_users(user_list):
    for user in user_list:
        print_user(user)

@app.route('/users/add', methods=('GET', 'POST'))
def add_user():
    g.active_url = '/users/add'
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        db = get_db()
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not role:
            error = 'Role is required.'
        elif db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {0} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password, role) VALUES (?, ?, ?)',
                (username, password, role)
            )
            db.commit()
            return redirect('/users')
        else:
            flash(error)

    return render_template('user/add-user.html')

@app.route('/users/<int:id>/edit', methods=('GET', 'POST'))
def edit_user(id):
    db = get_db()
    user = db.execute(
        'SELECT * FROM user WHERE id = ?', (id,)
    ).fetchone()
    print_user(user)

    error = None
    if user is None:
        error = 'User with ID={0} does not exist.'.format(id)
    else:
        print_user(user)

    if request.method == 'POST' and user:
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        db = get_db()
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not role:
            error = 'Role is required.'
        elif user['username'] != username and db.execute(
                'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'User {0} is already registered.'.format(username)

        if error is None:
            db.execute(
                'UPDATE user SET username = ?, password = ?, role= ? WHERE id = ?',
                (username, password, role, id)
            )
            db.commit()
            return redirect('/users')

    if error is not None:
        flash(error)

    return render_template('user/edit-user.html', user=user )

@app.route('/users/<int:id>/delete', methods=('POST',))
def delete_user(id):
    db = get_db()
    # if db.execute(
    #     'SELECT id FROM user WHERE id = ?', (id,)
    # ).fetchone() is not None:
    db.execute('DELETE FROM user WHERE id = ?', (id,))
    db.commit()

    return redirect(url_for('users'))


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

@app.route('/login', methods=('GET', 'POST'))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif user['password'] != password:
            error = 'Incorrect password.'

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session['user'] = {'id': user['id'], 'username': user['username'], 'role': user['role']}
            return redirect(url_for('home'))

        flash(error)

    return render_template('auth/login.html')

@app.route('/logout')
def logout():
    g.active_url = '/logout'
    session.clear()
    return render_template('home/home.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    g.active_url = '/register'
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = 'user'
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
                'INSERT INTO user (username, password, role) VALUES (?, ?, ?)',
                (username, password, role)
            )
            db.commit()
            return redirect('/login')
        else:
            flash(error)

    return render_template('auth/register.html')




if __name__ == '__main__':
    app.run()
