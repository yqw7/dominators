# import "packages" from flask
import requests
from __init__ import app
from redditapi import getRedditData
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response, Flask
from flask_restful import Api, Resource
from crud.model import Users
from __init__ import app
from templates.nicolas.gameapi import api_bp
from crud.app_crud import app_crud
from aboutus import aboutus
from crud.app_crud_api import app_crud_api

# create a Flask instance

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("walruses.html")


app.register_blueprint(app_crud)
app.register_blueprint(aboutus)
app.register_blueprint(app_crud_api)

@app.route('/postoftheday/')
def postoftheday():
    return render_template("postoftheday.html", rdata=getRedditData())

class_list = []
f = open("class_list.txt", "r")
for x in f:
    class_list.append(x)

def search_word(word):
    found_classes = []
    for i in class_list:
        if i.find(word) >= 0:
            found_classes.append(i)
    return found_classes

@app.route('/sandbox/', methods=['GET', 'POST'])
def sandbox():
    if request.form:
        term = request.form.get("name")
        searched = search_word(term)
        try:
            if len(term) != 0:  # input field has content
                return render_template("ethan/sandbox.html", class_list=class_list, name=searched)
        except:
            return render_template("404.html")
        # starting and empty input default
    return render_template("ethan/sandbox.html", class_list=class_list, name=" ")

@app.route('/ethan Create Task/')
def ethan_create_task():
    return render_template("/ethan/ethan_create_task.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/', methods=['GET', 'POST'])
def walruses():
    defaultURL = "walruses.html"
    if request.form:
        search_name = request.form.get("name")
        searched = search_word(search_name)
        name_list = ["ethan", "nicolas", "hassan", "calissa", "isabella"]
        url_list = ['ethan/Ethan.html', 'nicolas/nicolas.html', 'abouthassan.html', 'calissa.html', 'isabella.html']
        try:
            # name_index = name_list.index(search_name)
            if len(search_name) != 0:  # input field has content
                return render_template(defaultURL, class_list1=class_list, name=searched)
        except:
            return render_template("404.html")
    # starting and empty input default
    return render_template(defaultURL, class_list1=class_list, name=" ")


 
@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")

@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('/register/', methods=["GET", "POST"])

def register():
  return render_template("register.html")

#classes
@app.route('/apcsp/')
def signup():
    return render_template("classpages/apcsp.html")

@app.route('/hpoe/')
def hpoe():
    return render_template("classpages/hpoe.html")

@app.route('/apstudioart/')
def apstudioart():
    return render_template("classpages/apstudioart.html")
####

@app.route('/classes/')
def classes():
    return render_template("classes.html")

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

@app.route('/quiz')
def quiz():
    return render_template("quiz.html")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True,port=8000)