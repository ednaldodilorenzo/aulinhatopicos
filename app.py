from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world depois do push"

@app.route("/pelogit")
def pelogit():
    return "Essa rota foi adicionada pelo GIT"

@app.route("/teste")
def teste():
    return "Isso é um teste"

@app.route("/outra")
def outra():
    return "Outra rota"

if __name__ == "__main__":
    app.run()
