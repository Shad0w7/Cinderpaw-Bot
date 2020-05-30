# warriors.py

import discord
from discord.ext import commands
import datetime
import sys
from resourceScripts.pickname import *
from resourceScripts.randomCat import *
from resourceScripts.ships import *

class Warriors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # -- Random Cat, inherits from names.py --
    @commands.command(name='warriorname', help='Generate a Warrior Name!')
    async def warriorname(self, ctx):
        await ctx.send(warriorName())
        pass


    @commands.command(name='clanname', help='Generate a Clan Name!')
    async def clanname(self, ctx):
        await ctx.send(clanName())
        pass


    @commands.command(name='kittyname', help='Generate a Kittypet Name!')
    async def kittypetname(self, ctx):
        await ctx.send(kittypetName())
        pass


    # -- Random Image, inherits from randomCat.py --
    @commands.command(name='WarriorCat', help='returns random real cat picture!')
    async def randomcat(self, ctx):
        await ctx.send(randomCat())
        pass

    # -- Ships, inherits from ships.py --
    @commands.command(name='ship', help='Do a ship, with the two names together and a "*" between them (Use Full Name). Example, $ship Firestar*Sandstorm')
    async def ship(self, ctx, arg):
        shipValue = ship(arg.split('*')[0], arg.split('*')[1])
        await ctx.send(":heartpulse: :heartpulse: {0} x {1} is {2}%!!! :heartpulse: :heartpulse:".format(arg.split('*')[0], arg.split('*')[1], shipValue))    

def setup(bot):
    bot.add_cog(Warriors(bot))