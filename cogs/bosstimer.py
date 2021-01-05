# bosstimer.py
import os
import discord
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SCOPE = os.getenv('SLASH_SCOPE')

# Cog begin
class BossTimer(commands.Cog):

    def __init__(self, client):
        self.client = client

    url = SCOPE

    json = {
        "name": "setup",
        "description": "Initialize BOSS spawn timer with default values"
    }

    headers = {
        "Authorization": TOKEN 
    }


# Cog ending
def setup(client):
    client.add_cog(BossTimer(client))

