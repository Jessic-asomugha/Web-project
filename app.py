from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Test, test yup the pipeline is working!"
