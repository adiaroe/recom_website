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

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/reclist", methods=['POST'])
def reclist():
	userId = request.form['userId']
	genre = request.form['genre']
	print (type(genre))
	if genre == "Genre List":
		print ("in if")
		url = "http://35.170.52.162/recommendations/"+userId
		res = requests.get(url)
		data = res.json()
		l=[]
		for x in data:
			l.append(x["movie_name"])
		return render_template("reclist.html", movies=l)
	else:
		print ("in else")
		ext = userId+'-'+genre
		url = "http://35.170.52.162/genrerecommendations/"+ext
		res = requests.get(url)
		data = res.json()
		l=[]
		for x in data:
			l.append(x["movie_name"])
		return render_template("reclist.html", movies=l)

@app.route("/predict", methods=['POST'])
def predict():
	movieId = request.form['movieId']
	userId = request.form['userId']
	ext = userId+'-'+movieId
	url = "http://35.170.52.162/predict/1-500"
	res = requests.get(url)
	data = res.json()
	return render_template("test.html", y=data["product"], z=data["rating"])

@app.route("/test")
def test():
	x = 25
	return render_template("index.html", y=x)

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

if __name__ == "__main__":
    app.run(debug=True)