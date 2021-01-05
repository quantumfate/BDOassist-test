# bot.py
import os

import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix='!')

#client = discord.Client()

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD) 
    
    print(
        f'{client.user} has connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# Commands
@client.command(aliases=['load'])
@commands.has_permissions(administrator=True)
async def _load(ctx, extension):
    """Command: Loads the specified Cog"""

    client.load_extension(f'cogs.{extension}')
    await ctx.send(embed=discord.Embed(title="Loaded", color=0xb64bb3))


@client.command(aliases=['unload'])
@commands.has_permissions(administrator=True)
async def _unload(ctx, extension):
    """Command: Unloads the specified Cog"""

    client.unload_extension(f'cogs.{extension}')
    await ctx.send(embed=discord.Embed(title="Unloaded", color=0xb64bb3))


@client.command(aliases=['reload'])
@commands.has_permissions(administrator=True)
async def _reload(ctx, extension):
    """Command: Reloads the specified Cog"""

    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(embed=discord.Embed(title="Reloaded", color=0xb64bb3))

# @bot.command(name='helping')
# async def help_user(ctx):
#     
#     await ctx.send('I will help lol')

#bot.run(TOKEN)
client.run(TOKEN)