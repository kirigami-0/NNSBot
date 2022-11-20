import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='n.', intents=intents)


@bot.event
async def on_ready():
    print("ボット起動")

try:
    bot.run(os.environ["TOKEN"])
except Exception as e:
    print(e.status_code)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def start():
    return "123"