from flask import Flask

app = Flask(__name__)


@app.route('/')
def default():
    return '<h1>Welcome to the blockchain</h1>'


app.run()
