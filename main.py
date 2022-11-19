print("始まり")
import discord
from discord.ext import commands

intents = discord.Intents.default()


bot = commands.Bot(command_prefix='n.', intents=intents)

@bot.event
async def on_ready():
    print("ボット起動")

bot.run('token')