# import "packages" from flask
from flask import Flask, render_template
from wikipedia import requests
from templates.nicolas.gameapi import api_bp

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

@app.route('/calissa/')
def calissa():
    return render_template("calissa.html")

@app.route('/nicolas/')
def nicolas():
    return render_template("nicolas/nicolas.html")

@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/game', methods=['GET', 'POST'])
def game():
    url = "http://localhost:5000/api/game"
    response = requests.request("GET", url)
    return render_template("nicolas/game.html", game=response.json())

app.register_blueprint(api_bp)

@app.route('/stub/')
def stub():
    return render_template("stub.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
