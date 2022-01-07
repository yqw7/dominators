# import "packages" from flask
import requests
from flask import Blueprint, render_template
from __init__ import app

#from wikipedia import requests
# create a Flask instance
aboutus = Blueprint('aboutus', __name__)

@app.route('/Ethan/')
def stub2():
    return render_template("Ethan.html")

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
    url = "https://free-epic-games.p.rapidapi.com/free"

    headers = {
    'x-rapidapi-host': "free-epic-games.p.rapidapi.com",
    'x-rapidapi-key': "7d45651254msh14a87f4a7f9175ep109af9jsn98eb11ed4c66"
}

    response = requests.request("GET", url, headers=headers)
    output = response.json()
    return render_template("nicolas/nicolas.html", soccer=output)
