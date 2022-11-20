import discord
import os
import json
from dotenv import load_dotenv
# from discord.ext import commands
from flask import Flask #, render_template, request, session
# from oauth import Oauth
load_dotenv()
json_load = json.load(open('cog.json', 'r'))

app = Flask(__name__)
app.config["SECRET_KEY"] = "test"

@app.route('/')
def home():
    # return render_template("index.html", discord_url= Oauth.discord_login_url)
    return "123"

# @app.route('/login')
# def login ():
#     code = request.args.get("code")
#     access_token = Oauth.get_access_token(code)
#     session["token"] = access_token

#     user = Oauth.get_user_json(access_token)
#     user_name, user_id = user.get("username"), user.get("discriminator")
#     return f"成功 {user_name}#{access_token}"


if __name__ == '__main__':
    app.run(debug=True)



# bot = commands.Bot(command_prefix='n.', intents=discord.Intents.all())

# print("123456789")
# @bot.event
# async def on_ready():
#     print("ボット起動")
#     for cog_name in json_load["cog"]:
#         print(cog_name)
#         await bot.load_extension(f"Cog.{cog_name}")
#         return "123456789"

# @app.route('/')
# def hello_world():
#     bot.run(os.getenv("TOKEN"))
#     return 'Hello, World!'