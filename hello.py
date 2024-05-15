from flask import Flask, render_template

# create ad flask instance
app = Flask(__name__)


# create a route decorator
@app.route('/')
def index():
    return render_template("home.html")


@app.route('/elonlar')
def elon():
    return render_template("elon.html")


@app.route('/yonalishlar')
def yonalish():
    return render_template("yonalishlar.html")


@app.route('/jadval')
def jadval():
    return render_template("jadval.html")


@app.route('/nazoratlar')
def nazorat():
    return render_template("nazoratlar.html")


@app.route('/yakuniy')
def yakuniy():
    return render_template("yakuniy.html")


@app.route('/murojaat')
def murojaat():
    return render_template("murojaat.html")



