# bosstimer.py
import discord

from discord.ext import commands


# Cog begin
class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command("help")

    @commands.command(aliases=['help'])
    async def _user_help(self, ctx):
        """Command: Provides user with information"""

        await ctx.send(embed=discord.Embed(title="Help", color=0xb64bb3))

# Cog ending
def setup(client):
    client.add_cog(Help(client))





