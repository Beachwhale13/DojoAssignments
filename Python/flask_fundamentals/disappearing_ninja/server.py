from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/ninjas',methods=['POST'])
def results():
    return render_template("ninjas.html")


@app.route('/ninjas/<color>',methods=['POST'])
def color(color):
    color = request.form['color']
    if color == "red":
        return render_template("red.html")
    elif color == "blue":
        return render_template("blue.html")
    elif color == "orange":
        return render_template("orange.html")
    elif color == "purple":
        return render_template("purple.html")
    else:
        return render_template("april.html")



app.run(debug=True)
