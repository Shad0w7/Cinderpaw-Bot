# developer.py

import discord
from discord.ext import commands
import datetime
import os
VERSION = os.getenv('VERSION')

class DeveloperTools(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='myID', help='Returns User ID')
    async def myID(self, ctx):
        id = ctx.author.id
        await ctx.send("`>> Your ID is {0}`".format(id))
        pass

    @commands.command(name='test', help='Prints test message')
    async def test(self, ctx):
        await ctx.send("`>> Test Successful!`")
        pass

    @commands.command(name='version', help='Prints Version of the Bot Running!')
    async def version(self, ctx):
        await ctx.send('`>> Token and ENV Version: {0}`'.format(VERSION))
        pass

    @commands.command(name='bottime', help='Prints Current Bot Time')
    async def bottime(self, ctx):
        await ctx.send('`>> Bot Time is: {0}`'.format(datetime.datetime.now()))
        pass

    @commands.command(name='github', help='Prints Repo Information')
    async def bottime(self, ctx):
        await ctx.send('Cinderpaw is Open Source! This means the code is avaliable to view at: ```https://github.com/Shad0w7/Cinderpaw-Bot```')
        pass
    
def setup(bot):
    bot.add_cog(DeveloperTools(bot))