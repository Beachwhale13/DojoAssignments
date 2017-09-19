from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "secret secret"

mysql = MySQLConnector(app, 'users')

@app.route('/', methods=["GET"])
def getallusers():
    return redirect('/users')

@app.route('/users')
def index():
    query = "SELECT first_name, last_name, id AS id, email, MONTHNAME(created_at) AS month, DAY(created_at) AS day, YEAR(created_at) AS year FROM users"
    users = mysql.query_db(query)
    return render_template('index.html', users = users)

@app.route('/users/new')
def adduser():
    return render_template('new.html')

@app.route('/users/create', methods=["POST"])
def createuser():
    form = request.form
    data = {
        'first_name':form['first_name'],
        'last_name':form['last_name'],
        'email':form['email'],
    }
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<id>/show')
def show(id):
    data = {'id': id}
    query = "SELECT * FROM users WHERE id = :id"
    info = mysql.query_db(query, data)
    return render_template('show.html', info = info)

@app.route('/users/<id>/edit')
def editform(id):
    return render_template('edit.html', id = id)

@app.route('/users/<id>/update', methods=["POST"])
def update(id):
    form = request.form
    data = {
        'first_name':form['first_name'],
        'last_name':form['last_name'],
        'email':form['email'],
        'id':id
    }
    query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email=:email WHERE id = :id"
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<id>/delete')
def delete(id):
    data = {'id':id}
    query = "DELETE FROM users WHERE id = :id"
    mysql.query_db(query,data)
    return redirect('/users')

app.run(debug=True)
