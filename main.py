# import "packages" from flask
import requests
from flask import Flask, render_template, request
from redditapi import getRedditData
from flask import Flask, render_template
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
from crud.model import Users
#from wikipedia import requests
from templates.nicolas.gameapi import api_bp

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Ethan/')
def stub2():
    url = "https://api.kuroganehammer.com/api/characters"
    api = "https://api.kuroganehammer.com/api/characters/27/throws"

    response2 = requests.request("GET", api)
    new_text = response2.json() 
    
    response = requests.request("GET", url)
    text = response.json()
    return render_template("/ethan/Ethan.html", text=text, new_text=new_text)

@app.route('/smashapi/')
def smashapi():
    url = "https://api.kuroganehammer.com/api/characters"
    response = requests.request("GET", url)
    text = response.json()
    return render_template("/ethan/smashapi.html",text=text)

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


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/game', methods=['GET', 'POST'])
def game():
    url = "http://localhost:5000/api/game"
    response = requests.request("GET", url)
    return render_template("nicolas/game.html", game=response.json())









# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_crud = Blueprint('crud', __name__,
                     url_prefix='/crud',
                     template_folder='templates/crud/',
                     static_folder='static',
                     static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crud)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Blueprint)
    3.) API routes
    4.) API testing
"""

""" Users table queries"""


# User/Users extraction from SQL
def users_all():
    """converts Users table into JSON list """
    return [peep.read() for peep in Users.query.all()]


def users_ilike(term):
    """filter Users table by term into JSON list """
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Users.query.filter((Users.name.ilike(term)) | (Users.email.ilike(term)))
    return [peep.read() for peep in table]


# User extraction from SQL
def user_by_id(userid):
    """finds User in table matching userid """
    return Users.query.filter_by(userID=userid).first()


# User extraction from SQL
def user_by_email(email):
    """finds User in table matching email """
    return Users.query.filter_by(email=email).first()


""" app route section """


# Default URL
@app_crud.route('/')
def crud():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud.html", table=users_all())


# CRUD create/add
@app_crud.route('/create/', methods=["POST"])
def create():
    """gets data from form and add it to Users table"""
    if request.form:
        po = Users(
            request.form.get("name"),
            request.form.get("email"),
            request.form.get("password"),
            request.form.get("phone")
        )
        po.create()
    return redirect(url_for('crud.crud'))


# CRUD read
@app_crud.route('/read/', methods=["POST"])
def read():
    """gets userid from form and obtains corresponding data from Users table"""
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crud.html", table=table)


# CRUD update
@app_crud.route('/update/', methods=["POST"])
def update():
    """gets userid and name from form and filters and then data in  Users table"""
    if request.form:
        userid = request.form.get("userid")
        name = request.form.get("name")
        po = user_by_id(userid)
        if po is not None:
            po.update(name)
    return redirect(url_for('crud.crud'))


# CRUD delete
@app_crud.route('/delete/', methods=["POST"])
def delete():
    """gets userid from form delete corresponding record from Users table"""
    if request.form:
        userid = request.form.get("userid")
        po = user_by_id(userid)
        if po is not None:
            po.delete()
    return redirect(url_for('crud.crud'))


# Search Form
@app_crud.route('/search/')
def search():
    """loads form to search Users data"""
    return render_template("search.html")


# Search request and response
@app_crud.route('/search/term/', methods=["POST"])
def search_term():
    """ obtain term/search request """
    req = request.get_json()
    term = req['term']
    response = make_response(jsonify(users_ilike(term)), 200)
    return response


""" API routes section """


class UsersAPI:
    # class for create/post
    class _Create(Resource):
        def post(self, name, email, password, phone):
            po = Users(name, email, password, phone)
            person = po.create()
            if person:
                return person.read()
            return {'message': f'Processed {name}, either a format error or {email} is duplicate'}, 210

    # class for read/get
    class _Read(Resource):
        def get(self):
            return users_all()

    # class for read/get
    class _ReadILike(Resource):
        def get(self, term):
            return users_ilike(term)

    # class for update/put
    class _Update(Resource):
        def put(self, email, name):
            po = user_by_email(email)
            if po is None:
                return {'message': f"{email} is not found"}, 210
            po.update(name)
            return po.read()

    class _UpdateAll(Resource):
        def put(self, email, name, password, phone):
            po = user_by_email(email)
            if po is None:
                return {'message': f"{email} is not found"}, 210
            po.update(name, password, phone)
            return po.read()

    # class for delete
    class _Delete(Resource):
        def delete(self, userid):
            po = user_by_id(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            po.delete()
            return data

    # building RESTapi resource
    api.add_resource(_Create, '/create/<string:name>/<string:email>/<string:password>/<string:phone>')
    api.add_resource(_Read, '/read/')
    api.add_resource(_ReadILike, '/read/ilike/<string:term>')
    api.add_resource(_Update, '/update/<string:email>/<string:name>')
    api.add_resource(_UpdateAll, '/update/<string:email>/<string:name>/<string:password>/<string:phone>')
    api.add_resource(_Delete, '/delete/<int:userid>')


""" API testing section """


def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/crud'

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flintstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/create/Fred Flintstone/fred@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/read/ilike/John', "get"],
        ['/read/ilike/com', "get"],
        ['/update/wilma@bedrock.org/Wilma S Flintstone/123wsfli/0001112229', "put"],
        ['/update/wilma@bedrock.org/Wilma Slaghoople Flintstone', "put"],
        ['/delete/4', "delete"],
        ['/delete/5', "delete"],
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")


def api_printer():
    print()
    print("Users table")
    for user in users_all():
        print(user)

app.register_blueprint(api_bp)

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)