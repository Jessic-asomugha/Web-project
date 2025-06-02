from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Test, test yup the pipeline is working!"
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
