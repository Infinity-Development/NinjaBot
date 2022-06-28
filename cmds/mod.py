import datetime
import discord

from discord.ext import commands

warns = {}

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def warn(self, ctx: commands.Context, member: discord.Member, *, reason: str = None):
        await ctx.send(f"{member.mention}, you have been warned for {reason}")
        if member.id not in warns:
            warns[member.id] = []
        warns[member.id].append({"reason": reason, "by": ctx.author.id, "time": datetime.datetime.now()})
        await ctx.say(f"Warning ID: {len(warns[member.id]) - 1}")

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def delwarn(self, ctx: commands.Context, member: discord.Member, index: int, *, reason: str = None):
        await ctx.send(f"{member.mention}, you have had a warning removed for {reason}")
        if member.id not in warns:
            warns[member.id] = []
        del warns[member.id][index]

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def listwarns(self, ctx: commands.Context, member: discord.Member, *, reason: str = None):
        if member.id not in warns:
            warns[member.id] = []
        await ctx.send(f"{member.mention}:\n\n{str(warns[member.id])}")

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