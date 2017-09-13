from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "secretgame"
import random

@app.route ('/')
def index():
    if 'activities' not in session:
        session['activities'] = []

    print session['activities']

    return render_template("index.html")

@app.route('/process', methods=['POST'])
def rochambo():
    if "win" not in session:
        session['win'] = 0
    if "loss" not in session:
        session['loss'] = 0
    if "tie" not in session:
        session['tie'] = 0

    cpu_choice = random.choice(['rock', 'paper', 'scissors'])
    my_choice = request.form['game']
    wlt = 'win'
    if (cpu_choice == "rock"):
        if(my_choice == "rock"):
            session['tie'] += 1
            wlt = "tie"
        elif(my_choice == "paper"):
            session['win'] += 1
            wlt = "win"
        else:
            session['loss'] +=1
            wlt = "loss"
    if (cpu_choice == "scissors"):
        if(my_choice == "scissors"):
            session['tie'] += 1
            wlt = "tie"
        elif(my_choice == "rock"):
            session['win'] += 1
            wlt = "win"
        else:
            session['loss'] +=1
            wlt = "loss"
    if (cpu_choice == "paper"):
        if(my_choice == "paper"):
            session['tie'] += 1
            wlt = "tie"
        elif(my_choice == "scissors"):
            session['win'] += 1
            wlt = "win"
        else:
            session['loss'] +=1
            wlt = "loss"

    activity = "You choose {}. Computer chose {}. You {}".format(my_choice, cpu_choice, wlt)
    list_of_activities = session['activities']
    session['activities'].append(activity)
    session['activities'] = list_of_activities


    return redirect('/')

app.run(debug=True)
