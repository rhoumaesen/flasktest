from flask import Flask

app = Flask(__name__)
print("hello test")
@app.route("/")
def hello():
    return "hello world. "

if __name__ == "__main__":
    app.run("0.0.0.0")
