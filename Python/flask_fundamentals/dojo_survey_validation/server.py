from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "mysecretkey1"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result',methods=['POST'])
def results():
    if len(request.form['name']) < 1:
        flash("Name cannot be blank")
    elif len(request.form['name']) > 120:
        flash("Please enter a valid name")
    else:
        session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    if len(request.form['comment']) < 1:
        flash("Please enter a comment")
    else:
        session['comment'] = request.form['comment']
    return render_template("result.html")

@app.route('/reset', methods=["POST"])
def reset():
    return redirect("/")

app.run(debug=True)
