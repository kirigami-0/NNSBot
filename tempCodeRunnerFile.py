
bot = commands.Bot(command_prefix='n.', intents=intents)

@bot.event
async def on_ready():
    print("ボット起動")

bot.run(os.environ["TOKEN"])