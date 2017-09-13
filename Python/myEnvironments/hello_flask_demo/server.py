from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'great_secret1234'

@app.route('/')
def index():
    if "interests" not in session:
        session['interests'] = []

    print session['interests']
    list_of_fun_things = ["coding", "rapping", "napping"]

    return render_template('index.html', interests=session['interests'])

@app.route('/interests', methods=["POST"])
def add_interest():
    new_one =  request.form['new_interest']


    list_of_interests = session['interests']
    session['interests'].append(new_one)
    session['interests'] = list_of_interests

    return redirect('/')


app.run(debug=True)
