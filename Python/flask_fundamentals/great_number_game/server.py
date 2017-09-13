from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "ThisisSecret1"

answer = random.randrange(0,101)
@app.route('/')
def index():
    if 'guesses' not in session:
        session['guesses'] = []
    if len(session['guesses']) > 1:
        session['guesses'].pop(0)

    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    guess = int(request.form['guess'])
    diff = "boom"
    if (guess < answer):
        diff = "too low"
    elif (guess > answer):
        diff = "too high"
    else:
        diff = "right!"

    my_guess = "You guessed {}. Your answer is {}.".format(guess, diff)

    list_of_guesses = session['guesses']
    session['guesses'].append(my_guess)
    session['guesses'] = list_of_guesses

    return redirect('/')


@app.route('/reset', methods=["POST"])
def reset():
    answer = random.randrange(0,101)
    return render_template("index.html")

app.run(debug=True)
