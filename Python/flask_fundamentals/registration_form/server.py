from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "mysecretkey1"
import re
from datetime import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'\d.*[A-Z]|[A-Z].*\d')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=["POST"])
def validate():
    if len(request.form['first_name']) < 1:
        flash("First name cannot be blank")
        return redirect('/')
    elif str.isalpha(str(request.form['first_name'])) == False:
        flash("Invalid First name. Only Letters Please")
        return redirect('/')

    if len(request.form['last_name']) < 1:
        flash("Last name cannot be blank")
        return redirect('/')
    elif str.isalpha(str(request.form['last_name'])) == False:
        flash("Invalid Last name. Only Letters Please")
        return redirect('/')

    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email")

    if len(request.form['password']) < 1:
        flash("Password cannot be blank")
    elif len(request.form['password']) < 8:
        flash("Password must be longer than 8 characters")
    elif request.form['password'] != request.form['confirm_password']:
        flash("Your passwords do not match")
    elif not PASS_REGEX.match(request.form['password']):
        flash("Your password needs to have at least one number and one letter")

    inputDate = request.form['birthday']
    day,month,year = inputDate.split('/')
    print day, month, year
    if year > 2016:
        flash("Your year is invalid")
    if month > 12:
        flash("Your month is invalid")
    if day > 31:
        flash("Your date is invalid")

    flash("Thanks for submitting your information")
    return redirect('/')



app.run(debug=True)
