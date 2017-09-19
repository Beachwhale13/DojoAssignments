from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "secretkey"
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def email():
    errors = []
    if len(request.form['email']) == 0:
        errors.append("E-mail cannot be blank.")
    elif not EMAIL_REGEX.match(request.form['email']):
        errors.append("Please enter a valid e-mail.")

    if len(errors) > 0:
        for error in errors:
            flash(error)
        return redirect('/')
    else:
        data = {
            "email": request.form['email'],
        }

        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        mysql.query_db(query, data)
        return redirect('/success')

    return redirect('/')

@app.route('/success')
def success():
    query = "SELECT * FROM emails"
    emails = mysql.query_db(query)

    return render_template('success.html', emails = emails)

@app.route('/emails/<id>/delete')
def delete_user(id):
    data = {'id': id}
    query = 'DELETE FROM emails WHERE id = :id'
    mysql.query_db(query, data)
    return redirect('/success')

app.run(debug=True)
