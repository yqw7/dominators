# import "packages" from flask
from flask import Flask, render_template
import requests
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Ethan/')
def stub2():
    return render_template("Ethan.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")

@app.route('/abouthassan/')
def abouthassan():
    return render_template("abouthassan.html")

@app.route('/isabella/')
def isabella():
    return render_template("isabella.html")



@app.route('/nicolas/')
def nicolas():
    return render_template("nicolas.html")

@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
