import datetime
import discord

from discord.ext import commands

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def warn(self, ctx: commands.Context, member: discord.Member, *, reason: str = None):
        await ctx.send(f"{member.mention}, you have been warned for {reason}")

    @commands.command()
    async def kick(self, ctx: commands.Context, member: discord.Member, *, reason: str = None):
        """Kicks a member"""
        try:
            await member.timeout(datetime.timedelta(minutes = 10), reason=reason)
        except:
            ...
        await ctx.send("Kicked member")

    @commands.command()
    @commands.bot_has_permissions(administrator=True)
    async def timeout(self, ctx: commands.Context, member: discord.Member, seconds: int, *, reason=None):
        """Times out a member"""
        await member.timeout(datetime.timedelta(minutes = seconds), reason=reason)
        await ctx.say("Timed out member")

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandNotFound):
            return
        await ctx.send(str(error))

async def setup(bot: commands.Bot):
    await bot.add_cog(Mod(bot))
    return bot