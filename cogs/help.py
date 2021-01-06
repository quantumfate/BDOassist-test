# bosstimer.py
import os

from discord.ext.commands import Cog
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='!')

# Cog begin
class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command("help")



# Cog ending
def setup(client):
    client.add_cog(Help(client))





