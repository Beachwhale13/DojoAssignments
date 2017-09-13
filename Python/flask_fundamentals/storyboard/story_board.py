from flask import Flask, render_template,redirect, session

app = Flask(__name__)
app.secret_key = "mysecretkey"

course = 0
@app.route('/')
def index():
    session['course'] += 1
    if session['course'] == 2:
        return render_template('ramenAllDay.html')
    elif session['course'] == 3:
        return render_template('kbbq.html')
    elif session['course'] == 4:
        return render_template('mochi.html')
    elif session['course'] == 5:
        return render_template('tasty.html')

    return render_template('index.html')

@app.route('/poison', methods = ["post"])
def poison():
    return render_template('poison.html')

@app.route('/reset', methods = ["post"])
def reset():
    return redirect('/')

#
# def my_projects():
#     return render_template('my_projects.html')

# @app.route('/about')
# def I_am_a():
#     return render_template('I_am_a.html')

app.run(debug=True)
