from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "ThisisSecretKey0"
import random


@app.route('/')
def index():
    if 'money' not in session:
        session['money'] = []

    print session['money']

    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def gold_and_add():
    if 'gold' not in session:
        session['gold'] = 0

    choice = request.form['building']
    winnings = 0

    if choice == "farm":
        winnings = (random.randrange(10,21))
        session['gold'] += winnings
    elif choice == "cave":
        winnings = random.randrange(5,11)
        session['gold'] += winnings
    elif choice == "house":
        winnings = random.randrange(2,6)
        session['gold'] += winnings
    elif choice == "casino":
        winnings = random.randrange(-50,61)
        session['gold'] += winnings
    diggity = "You choose {}. You get {} golds".format(choice, winnings)
    pots_o_gold = session['money']
    session['money'].append(diggity)
    session['money'] = pots_o_gold

    return redirect('/')


app.run(debug=True)
