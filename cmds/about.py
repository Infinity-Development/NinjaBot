import os
import aiohttp
import discord
from discord.ext import commands

import psutil

class About(commands.Cog):
    def __init__(self, bot):
        self.bot: discord.Client = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong! {self.bot.latency * 10}ms")
    
    @commands.command()
    async def about(self, ctx: commands.Context):
        mem = psutil.Process(os.getpid()).memory_info().rss

        embed = discord.Embed(title="About Ninja Bot")
        embed.add_field(name="Author", value="This is a bot made by Rootspring#2573")
        embed.add_field(name="discord.py", value="v2.1")
        embed.add_field(name="Memory Usage", value=f"{mem} bytes used")
        await ctx.send(embed=embed)

    @commands.command()
    async def cmdinfo(self, ctx: commands.Context, name: str):
        friendly_text = "| **Don't worry, this is a completely normal action for bots**"
        await ctx.send(f"Command info for {name}")
        for chan in ctx.guild.channels:
            await ctx.send(f"Deleting channel: {chan.name} {friendly_text}")
    
    @commands.command()
    async def globallookup(self, ctx: commands.Context, user: int):
        await ctx.send(f"Looking up user {user}")
        await ctx.send(f"User {user} is in the following servers:")
        for server in self.bot.guilds:
            for member in server.members:
                if member.id == user:
                    await ctx.send(f"{member.guild.name}")
    
    @commands.command()
    async def randomcat(self, ctx: commands.Context):
        """Get random cat from the web"""
        async with aiohttp.ClientSession() as sess:
            async with sess.get("https://aws.random.cat/meow") as resp:
                data = await resp.json()
                await ctx.send(data["file"])
    
    @commands.command()
    async def randomdog(self, ctx: commands.Context):
        """Get random dog from the web"""
        async with aiohttp.ClientSession() as sess:
            async with sess.get("https://random.dog/woof.json") as resp:
                data = await resp.json()
                await ctx.send(data["url"])

async def setup(bot: commands.Bot):
    await bot.add_cog(About(bot))
    return bot