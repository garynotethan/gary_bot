import discord
from discord.ext import commands

class Videos(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sls(self, ctx):
        await ctx.send('https://www.youtube.com/playlist?list=PLqvo4PPYx7nU8j3Cjz2u6dZ7s0FERNJ7y')

    @commands.command()
    async def links1(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=4RZDt9B4sfQ')

    @commands.command()
    async def links2(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=24CxVVMact4')

    @commands.command()
    async def cvs(self, ctx):
        await ctx.send('https://www.youtube.com/playlist?list=PLE4F7122D79474299 I recommend watching a bunch of cvs to get some inspiration! It\'s also a great way to develop spinning preferences and see potential areas you want to explore.')

    @commands.command(aliases=['sonic'])
    async def sonictut(self, ctx):
        await ctx.send('https://youtu.be/IyfvQbepErw')

    @commands.command(aliases=['bust', 'busttutorial'])
    async def busttut(self, ctx):
        await ctx.send('These are gary approved bust tutorials. \n https://www.youtube.com/watch?v=TUYpVo14lWo \n https://www.youtube.com/watch?v=0yL7hn011V8&t \n https://www.youtube.com/watch?v=UvyNfif6Kdo')

    @commands.command(aliases=['g2', 'g2removal', 'g2grips'])
    async def g2grip(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=HNZhY6q8Aw0')

    @commands.command(aliases=['walmartmod', 'walmart', 'walmartmodv1', 'garywalmartmod1', 'walmartmod1', ])
    async def garywalmartmod(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=xJl72ZisCVw')

    @commands.command()
    async def links3(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=sJjx797j1x8')
    
    @commands.command()
    async def links(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=4RZDt9B4sfQ\nhttps://www.youtube.com/watch?v=24CxVVMact4\nhttps://www.youtube.com/watch?v=sJjx797j1x8')
    
    @commands.command(aliases=['staplesmod', 'staples', 'staplesmodv1', 'garystaplesmod1', 'staplesmod1',])
    async def garystaplesmod(self, ctx):
        await ctx.send('https://youtu.be/xgSxwK2zYpk')

    @commands.command()
    async def essentials(self, ctx):
        await ctx.send('This is playlist contains Gary\'s favourite penspinning videos and stuff he would recommend noobs watch aswell. https://youtube.com/playlist?list=PLkPBnIe5Br650sNllwRwlURZeBZDAjSrb')
        
    @commands.command()
    async def chopstick(self, ctx):
        await ctx.send('https://youtu.be/9bAevHmu9oE')
    
    @commands.command(aliases=['st'])
    async def supertip(self, ctx):
        await ctx.send('https://youtu.be/ep6MSDCFHm0')
    
async def setup(bot):
    await bot.add_cog(Videos(bot))
