from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "secret secret"
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

mysql = MySQLConnector(app, 'loginandregistration')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/validate', methods=["POST"])
def validation():
    form = request.form
    errors = []

    if(form['action'] == 'Register'):
        if len(form['first_name']) <= 2:
            errors.append("Please enter a valid first name")
        if any([letter.isdigit() for letter in form['first_name']]):
            errors.append("Please enter an alphanumeric first name")
        if len(form['last_name']) <= 2:
            errors.append("Please enter a valid last name")
        if any([letter.isdigit() for letter in form['last_name']]):
            errors.append("Please enter an alphanumeric last name")
        if not EMAIL_REGEX.match(form['email']):
            errors.append("Please enter a valid email")
        if len(form['password']) == 0:
            errors.append("Please enter a password")
        else:
            if len(form['password']) < 8:
                errors.append("Password must be at least 8 characters.")
        if form['password'] != form['passconf']:
            errors.append('Password and confirmation fields must match.')

        if len(errors) > 0:
            for error in errors:
                flash(error)
        else:
            password = md5.new(form['password']).hexdigest()
            data = {
                "first_name": form['first_name'],
                'last_name': form['last_name'],
                'email': form['email'],
                'password': password
                }
            query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
            mysql.query_db(query, data)
            return render_template('success.html')
        return redirect('/')

    if(form['action'] == 'Login'):
        email = form['email']
        user_query = "SELECT * FROM users where users.email = :email LIMIT 1"
        query_data = {'email': email}
        user = mysql.query_db(user_query, query_data)

        if len(user) != 0:
            hash_pass = md5.new(form['password']).hexdigest()
            if user[0]['password'] == hash_pass:
                return render_template('success.html')
            else:
                errors.append("Email and password does not match")
        else:
            errors.append("Please enter a registered email")

        if len(errors) > 0:
            for error in errors:
                flash(error)
            return redirect('/')


app.run(debug=True)
