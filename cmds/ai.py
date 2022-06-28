import discord
from discord.ext import commands


class AI(commands.Cog):
    def __init__(self, bot):
        self.bot: discord.Client = bot
    
    @commands.command()
    async def pingai(self, ctx):
        await ctx.send(f"Pong! {round(self.bot.latency * 12142.241627391)}ms")
    
async def setup(bot: commands.Bot):
    await bot.add_cog(AI(bot))
    return bot