from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/outra")
def outra():
    return "Outra rota"

if __name__ == "__main__":
    app.run()
