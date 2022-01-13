# import "packages" from flask
import requests
from __init__ import app
from redditapi import getRedditData

from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response, Flask
from flask_restful import Api, Resource
from crud.model import Users
from __init__ import app
#from wikipedia import requests
from templates.nicolas.gameapi import api_bp
from crud.app_crud import app_crud
from aboutus import aboutus

# create a Flask instance

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


app.register_blueprint(app_crud)
app.register_blueprint(aboutus)

@app.route('/postoftheday/')
def postoftheday():
    return render_template("postoftheday.html", rdata=getRedditData())

@app.route('/sandbox/')
def sandbox():
    return render_template("ethan/sandbox.html")

# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses', methods=['GET', 'POST'])
def walruses():
    defaultURL = "walruses.html"
    if request.form:
        search_word = request.form.get("name")
        name_list = ["ethan", "nicolas", "hassan", "calissa", "isabella"]
        url_list = ['ethan/Ethan.html', 'nicolas/nicolas.html', 'abouthassan.html', 'calissa.html', 'isabella.html']
        try:
            name_index = name_list.index(search_word)
            if len(search_word) != 0 and name_index >= 0:  # input field has content
                return render_template(url_list[name_index])
        except:
            return render_template("404.html")
    # starting and empty input default
    return render_template(defaultURL)


 
@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route('/register/')
def signup():
    return render_template("register.html")

@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/game', methods=['GET', 'POST'])
def game():
    url = "http://localhost:5000/api/game"
    response = requests.request("GET", url)
    return render_template("nicolas/game.html", game=response.json())


app.register_blueprint(api_bp)

@app.errorhandler(404)
def page_not_found():
    # note that we set the 404 status explicitly
    return render_template('404.html')

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)