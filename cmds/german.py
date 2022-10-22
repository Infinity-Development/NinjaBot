import aiohttp
import discord
from discord.ext import commands

class German(commands.Cog):
    def __init__(self, bot):
        self.bot: discord.Client = bot
    
    @commands.command()
    async def nutzerinfo(self, ctx):
        embed = discord.Embed(colour=discord.Colour(0x359ae))
        if ctx.user.avatar is None:
            embed.set_footer(text=f"Informationen über {ctx.user}", icon_url=ctx.user.default_avatar.url)
        else:
            embed.set_footer(text=f"Informationen über {ctx.user}", icon_url=ctx.user.avatar.url)
        if user.avatar is None:
            embed.set_thumbnail(url=user.default_avatar.url)
        else:
            embed.set_thumbnail(url=user.avatar.url)
        embed.set_author(name=user)
        embed.add_field(name="ID:", value=user.id)
        embed.add_field(name="Diskriminator:", value=user.discriminator)
        embed.add_field(name="Roboter?", value=user.bot)
        embed.add_field(name="Anzeigename:", value=user.display_name)
        embed.add_field(name="Datum, an dem dieser Account dem Server beigetreten ist:", value=f"{user.joined_at.day}.{user.joined_at.month}.{user.joined_at.year}")
        embed.add_field(name="Datum, an dem dieser Account erstellet wurde:", value=f"{user.created_at.day}.{user.created_at.month}.{user.created_at.year}")
        roles = ""
        for role in reversed(user.roles):
            if (len(role.mention)+len(roles)+4) >= 1024:
                roles += "..."
                break
            else:
                if role.name != "@everyone":
                    roles += f"{role.mention}, "
                else:
                    roles += "@everyone"
        embed.add_field(name="Rollen:", value=roles, inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def notruf(self, ctx):
        await ctx.send("Es scheint als wäre ein Fehler aufgetreten!")
        
async def setup(bot: commands.Bot):
    await bot.add_cog(German(bot))
    return bot
