from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("qual o seu nome?")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Olá " + str(request.form['name_input']) + ", saudações humano!")
	return render_template("index.html")
