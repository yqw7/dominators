import requests, json


# import "packages" from flask
from flask import Flask, render_template

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
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    payload = "q=Hello%2C%20world!&target=es&source=en"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'accept-encoding': "application/gzip",
        'x-rapidapi-host': "google-translate1.p.rapidapi.com",
        'x-rapidapi-key': "d7c8c8031emshc7982f51947d6d4p19192fjsnc28f123f5152"
}

    response = requests.request("POST", url, data=payload, headers=headers)
    text = response.json()
    return render_template("calissa.html", text=text)


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
