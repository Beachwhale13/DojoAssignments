from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisisSecret"


counter = 0
@app.route('/')
def index():
    session['counter'] += 1
    return render_template('index.html')


@app.route('/bytwo', methods=["POST"])
def bytwo():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
