from flask import Flask, render_template, request

from flask import Flask, render_template

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

if __name__ == "__main__":
    app.run(debug=True)

# @app.route("/asd")
# def get():
#     try:
#         res = requests.get(http://3.80.144.140/recommendations/1)
#         return res.json()
#     except:
#         return False

#@app.route("/asd")
#data = get('http://3.80.144.140/recommendations/1')
#print(data)
