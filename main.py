# import "packages" from flask
import requests
from __init__ import app
from redditapi import getRedditData

from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response, Flask
from flask_restful import Api, Resource
from crud.model import Users
from __init__ import app
from wikipedia import requests
from templates.nicolas.gameapi import api_bp
from crud.app_crud import app_crud


# create a Flask instance

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Ethan/')
def stub2():
    return render_template("Ethan.html")

app.register_blueprint(app_crud)

@app.route('/calissa/')
def calissa():
    url = "https://burgers1.p.rapidapi.com/burgers"

    headers = {
        'x-rapidapi-host': "burgers1.p.rapidapi.com",
        'x-rapidapi-key': "d7c8c8031emshc7982f51947d6d4p19192fjsnc28f123f5152"
    }

    response = requests.request("GET", url, headers=headers)
    text = response.json()
    return render_template("calissa.html", text=text)

@app.route('/postoftheday/')
def postoftheday():
    return render_template("postoftheday.html", rdata=getRedditData())

# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")

@app.route('/abouthassan/')
def abouthassan():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "d13a89c0d8msh97a5f0a94e24845p145b38jsnee3109acb495"
    }

    response = requests.request("GET", url, headers=headers)
    text = response.json()
    return render_template("abouthassan.html", text=text)

@app.route('/isabella/')
def isabella():
    return render_template("isabella.html")

@app.route('/nicolas/')
def nicolas():
    return render_template("nicolas/nicolas.html")

@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('/signup/')
def signup():
    return render_template("signup.html")

@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/game', methods=['GET', 'POST'])
def game():
    url = "http://localhost:5000/api/game"
    response = requests.request("GET", url)
    return render_template("nicolas/game.html", game=response.json())


app.register_blueprint(api_bp)

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)