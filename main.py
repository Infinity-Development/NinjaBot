# Onboarding bot for v4

# This example requires the 'message_content' privileged intent to function.

# From https://github.com/Rapptz/discord.py/blob/master/examples/basic_voice.py

import asyncio
import importlib

import discord
import yt_dlp

import os

import dotenv 

dotenv.load_dotenv()

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    description='Testing bot',
    intents=intents,
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


async def main():
    async with bot:
        # Load all cogs from cmds folder
        for filename in os.listdir('./cmds'):
            if filename.endswith('.py'):
                print(f'Loading {filename}')
                await bot.load_extension(f'cmds.{filename[:-3]}')
        await bot.start(os.getenv("TOKEN"))


asyncio.run(main())