import discord
from discord.ext import commands
from discord import app_commands
class Videos(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def sls(self, ctx):
        await ctx.send('https://www.youtube.com/playlist?list=PLqvo4PPYx7nU8j3Cjz2u6dZ7s0FERNJ7y')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def links1(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=4RZDt9B4sfQ')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def links2(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=24CxVVMact4')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def cvs(self, ctx):
        await ctx.send('https://www.youtube.com/playlist?list=PLE4F7122D79474299 I recommend watching a bunch of cvs to get some inspiration! It\'s also a great way to develop spinning preferences and see potential areas you want to explore.')

    @commands.hybrid_command(aliases=['sonic'])
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def sonictut(self, ctx):
        await ctx.send('https://youtu.be/IyfvQbepErw')

    @commands.hybrid_command(aliases=['bust', 'busttutorial'])
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def busttut(self, ctx):
        await ctx.send('These are gary approved bust tutorials. \n https://www.youtube.com/watch?v=0yL7hn011V8&t \n https://www.youtube.com/watch?v=UvyNfif6Kdo')

    @commands.hybrid_command(aliases=['g2', 'g2removal', 'g2grips'])
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def g2grip(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=HNZhY6q8Aw0')

    @commands.hybrid_command(aliases=['walmartmod', 'walmart', 'walmartmodv1', 'garywalmartmod1', 'walmartmod1', ])
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def garywalmartmod(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=xJl72ZisCVw')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def links3(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=sJjx797j1x8')
    
    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def links(self, ctx):
        await ctx.send('https://www.youtube.com/watch?v=4RZDt9B4sfQ\nhttps://www.youtube.com/watch?v=24CxVVMact4\nhttps://www.youtube.com/watch?v=sJjx797j1x8')
    
    @commands.hybrid_command(aliases=['staplesmod', 'staples', 'staplesmodv1', 'garystaplesmod1', 'staplesmod1',])
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def garystaplesmod(self, ctx):
        await ctx.send('https://youtu.be/xgSxwK2zYpk')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def essentials(self, ctx):
        await ctx.send('This is playlist contains Gary\'s favourite penspinning videos and stuff he would recommend noobs watch aswell. https://youtube.com/playlist?list=PLkPBnIe5Br650sNllwRwlURZeBZDAjSrb')
        
    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def chopstick(self, ctx):
        await ctx.send('https://youtu.be/9bAevHmu9oE')
    
    @commands.hybrid_command(aliases=['st'])
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def supertip(self, ctx):
        await ctx.send('https://youtu.be/ep6MSDCFHm0')
    
async def setup(bot):
    await bot.add_cog(Videos(bot))
