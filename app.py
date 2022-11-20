import discord
import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(os.environ.get("TOKEN"))
    print("123456789")
    return 'Hello, World!'