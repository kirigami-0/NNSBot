from discord.ext import commands

class math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def math(self, ctx):
        await ctx.send("12456789")

async def setup(bot):
    await bot.add_cog(math(bot))
