# bosstimer.py
import os
import json
import discord
import time
import sched
import datetime

from discord.ext.commands import context
import requests

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Cog begin
class BossTimer(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.embedBoss = discord.Embed(title="Bosstimer", description="A boss has spawned.", color=0x00ff00)
        self.currentRegion = 'EU'

        with open('bosstimer.json') as f:
            self.bossData = json.load(f)

    def _build_field(self, dayTime, bossEvent):
        self.embedBoss.add_field(name="%s"%dayTime, value="%s"%bossEvent)

    @commands.command(aliases=['printboss'])
    async def _bossinfo(self, ctx):
        
        for key in self.bossData['%s'%self.currentRegion]:

            #currentTime = self.bossData['%s'%self.currentRegion][key][0]["time"]
            #currentBoss = self.bossData['%s'%self.currentRegion][key][0]["boss"]

            if self.date.today().to_s == "thursday": # & self.time.today().to_s == currentTime
                self.schedule.every(key).at("18:40").do(self._build_field(self, "thursday", "Kzarka"))


        await ctx.send(embed=self.embedBoss)

# Cog ending
def setup(client):
    client.add_cog(BossTimer(client))

