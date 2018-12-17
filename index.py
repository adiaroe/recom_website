from flask import Flask, render_template, request

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/registration")
def registration():
    return render_template("index.html")

@app.route("/reclist", methods=['POST'])
def reclist():
	name = request.form['name']
	return name

@app.route("/predict")
def get():
	ext = 500
	url = 'http://35.170.52.162/predict/'+repr(ext)
	res = requests.get(url)
	data = res.json()
	return "The rating of the movie "+repr(data['product'])+" is "+repr(data['rating'])

if __name__ == "__main__":
    app.run(debug=True)