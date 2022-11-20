from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("123456789")
    return 'Hello, World!'
