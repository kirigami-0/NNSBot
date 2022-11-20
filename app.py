import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

from flask import Flask
app = Flask(__name__)
bot = commands.Bot(command_prefix='n.', intents=discord.Intents.all())

@app.route('/')
def hello_world():
    
    # print(os.getenv("TOKEN"))
    # print("123456789")
    bot.run(os.getenv("TOKEN"))
    return 'Hello, World!'