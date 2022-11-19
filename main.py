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

bot.run(os.environ["TOKEN"])