import discord
from discord.ext import commands


class Servers(command.cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def planet(ctx):
        await ctx.send('https://discord.gg/5thTVupNHh')

    @commands.command()
    async def workshop(ctx):
        await ctx.send('https://discord.com/invite/7F4BjWD')

    @commands.command()
    async def ipmc(ctx):
        await ctx.send('https://discord.gg/wby7U2g')

    @commands.command()
    async def mpsd(ctx):
        await ctx.send('https://discord.gg/347xyYa')

    @commands.command()
    async def reddit(ctx):
        await ctx.send('https://discord.com/invite/010bWcQCla9sRdYea')

    @commands.command()
    async def psuk(ctx):
        await ctx.send('https://discord.gg/AE2WQrz5JM')

    @commands.command()
    async def kronen(ctx):
        await ctx.send('https://discord.gg/AZDeABYj74')

    @commands.command()
    async def spindys(ctx):
        await ctx.send('https://discord.gg/VzyYnfECnS')

    @commands.command()
    async def fenspinner(ctx):
        await ctx.send('https://discord.gg/9ERAUCDAkS')

    @commands.command(aliases=['india'])
    async def ibps(ctx):
        await ctx.send('https://discord.gg/tmFJMsbp7u')




#async def setup(bot):
#    await bot.add_cog(Servers(bot))






