import discord
from discord.ext import commands
from discord import app_commands

class Servers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def planet(self, ctx):
        await ctx.send('https://discord.gg/5thTVupNHh')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def workshop(self, ctx):
        await ctx.send('https://discord.com/invite/7F4BjWD')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ipmc(self, ctx):
        await ctx.send('https://discord.gg/wby7U2g')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def mpsd(self, ctx):
        await ctx.send('https://discord.gg/347xyYa')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def reddit(self, ctx):
        await ctx.send('https://discord.com/invite/010bWcQCla9sRdYea')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def psuk(self, ctx):
        await ctx.send('https://discord.gg/AE2WQrz5JM')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def kronen(self, ctx):
        await ctx.send('https://discord.gg/AZDeABYj74')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def spindys(self, ctx):
        await ctx.send('https://discord.gg/VzyYnfECnS')

    @commands.hybrid_command()
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def fenspinner(self, ctx):
        await ctx.send('https://discord.gg/Fz2zHWjn8G')

    @commands.hybrid_command(aliases=['india'])
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ibps(self, ctx):
        await ctx.send('https://discord.gg/tmFJMsbp7u')

    @commands.hybrid_command(aliases=['krug'])
    @app_commands.allowed_installs(guilds=True, users=True)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def krugdom(self, ctx):
        await ctx.send('https://discord.gg/eMQSvwDd5Q')

async def setup(bot):
    await bot.add_cog(Servers(bot))






