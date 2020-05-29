# randomimage.py

'''
For the Giphy integration
'''

import discord
from discord.ext import commands
import datetime
import os
import giphypop
from unsplash.api import Api
from unsplash.auth import Auth


VERSION = os.getenv('VERSION')
GIPHYKEY = os.getenv('GIPHYKEY')
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY')
UNSPLASH_SECRET_KEY = os.getenv('UNSPLASH_SECRET_KEY')
UNSPLASH_REDIRECT_URI = os.getenv('UNSPLASH_REDIRECT_URI')

# -- Initialize Photo Libraries

g = giphypop.Giphy(api_key = GIPHYKEY)

client_id = UNSPLASH_ACCESS_KEY
client_secret = UNSPLASH_SECRET_KEY 
redirect_uri = UNSPLASH_REDIRECT_URI
code = ""

auth = Auth(client_id, client_secret, redirect_uri, code=code)
api = Api(auth)


class RandomImage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # -- Giphy --

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

    # -- Unsplash --

    @commands.command(name='catimg', help='mrrow')
    async def catImg(self, ctx):
        id = ctx.author.id
        x = api.photo.random(query="cat")
        toReturn = 'https://unsplash.com/photos/' + str(x[0]).split("'")[1]
        await ctx.send("Your Random Cat is {}".format(toReturn))
        pass

    @commands.command(name='dogimg', help='woof')
    async def dogImg(self, ctx):
        id = ctx.author.id
        x = api.photo.random(query="dog")
        toReturn = 'https://unsplash.com/photos/' + str(x[0]).split("'")[1]
        await ctx.send("Your Random Dog is {}".format(toReturn))
        pass

    @commands.command(name='unsplash', help='search unsplash! [Still in Beta might raise exception]')
    async def searchImg(self, ctx, args):
        id = ctx.author.id
        x = api.photo.random(query=args)
        toReturn = 'https://unsplash.com/photos/' + str(x[0]).split("'")[1]
        await ctx.send("Result for your search: {}".format(toReturn))
        pass

    
def setup(bot):
    bot.add_cog(RandomImage(bot))