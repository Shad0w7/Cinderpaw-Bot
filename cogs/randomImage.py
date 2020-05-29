# randomimage.py

'''
For the Giphy integration
'''

import discord
from discord.ext import commands
import datetime
import os
import giphypop

VERSION = os.getenv('VERSION')
GIPHYKEY = os.getenv('GIPHYKEY')
g = giphypop.Giphy(api_key = GIPHYKEY)

class RandomImage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='gifcat', help='Returns random gif of cat')
    async def catgif(self, ctx):
        id = ctx.author.id
        returnVal = g.random_gif('cat')
        await ctx.send("Your Random Cat gif is:\n {}".format(returnVal.url))
        pass

    @commands.command(name='gifdog', help='Returns random gif of dog')
    async def doggif(self, ctx):
        id = ctx.author.id
        returnVal = g.random_gif('dog')
        await ctx.send("Your Random Dog gif is:\n {}".format(returnVal.url))
        pass

    @commands.command(name='elonmusk', help='i like tesla')
    async def musk(self, ctx):
        id = ctx.author.id
        returnVal = g.random_gif('elon musk')
        await ctx.send("All hail elon\n {}".format(returnVal.url))
        pass

    @commands.command(name='spaceship', help='VROOM!')
    async def rocket(self, ctx):
        id = ctx.author.id
        returnVal = g.random_gif('rocket')
        await ctx.send("VROOM:\n {}".format(returnVal.url))
        pass

    @commands.command(name='gif', help='Returns random gif of search value')
    async def gifsearch(self, ctx, args):
        id = ctx.author.id
        returnVal = g.random_gif(args)
        await ctx.send("Your Result for Term:{0}:\n {1}".format(args, returnVal.url))
        pass



    
def setup(bot):
    bot.add_cog(RandomImage(bot))