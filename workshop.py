from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(_name_)

# Configure the database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'examily'
app.config['MYSQL_DB'] = 'team_13'

# Create a new MySQL connection
mysql = MySQL(app)

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Mentor registration page route
@app.route('/mentors', methods=['GET', 'POST'])
def mentors():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO mentors (name, email) VALUES (%s, %s)', (name, email))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('mentors'))
    else:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM mentors')
        mentors = cur.fetchall()
        cur.close()
        return render_template('mentors.html', mentors=mentors)

# Session upload page route
@app.route('/sessions', methods=['GET', 'POST'])
def sessions():
    if request.method == 'POST':
        mentor_id = request.form
# Student registration page route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        session_id = request.form['session_id']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO registrations (email, session_id) VALUES (%s, %s)', (email, session_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('success'))
    else:
        cur = mysql.connection.cursor()
        cur.execute('SELECT sessions.id, mentors.name, sessions.title, sessions.description, sessions.date, sessions.time FROM sessions INNER JOIN mentors ON sessions.mentor_id = mentors.id')
        sessions = cur.fetchall()
        cur.close()
        return render_template('register.html', sessions=sessions)

# Success page route
@app.route('/success')
def success():
    return render_template('success.html')