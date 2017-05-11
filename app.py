from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/there")
def hello_there():
    return "Hello there!"

if __name__ == "__main__":
	app.run()