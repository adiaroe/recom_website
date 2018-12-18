from flask import Flask, flash, redirect, render_template, request, session, abort
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return "Movie Recommender App!"
 
@app.route("/recommendation")
def recommendation():
    return render_template('test.html')
 
if __name__ == "__main__":
    
    app.run()
	