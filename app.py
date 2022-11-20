import discord
import os
import json
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
json_load = json.load(open('cog.json', 'r'))

from flask import Flask
app = Flask(__name__)
bot = commands.Bot(command_prefix='n.', intents=discord.Intents.all())

@app.route('/')
async def hello_world():
    # @bot.event
    # async def on_ready():
    print("ボット起動")
    for cog_name in json_load["cog"]:
        print(cog_name)
        await bot.load_extension(f"Cog.{cog_name}")
    bot.run(os.getenv("TOKEN"))
    return 'Hello, World!'