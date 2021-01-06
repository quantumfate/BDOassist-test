# bosstimer.py
import discord

from discord.ext import commands


# Cog begin
class Autosetup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['autosetup'])
    async def _autosetup(self, ctx):
        """Command: Provides user with information"""

        await ctx.send(embed=discord.Embed(title="Setup", color=0xb64bb3))

# Cog ending
def setup(client):
    client.add_cog(Autosetup(client))