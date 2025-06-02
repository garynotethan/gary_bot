import discord
from discord.ext import commands
from discord import app_commands

class PS_Stores(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.hybrid_command()
    @app_commands.user_install()
    async def penstock(self, ctx):
        await ctx.send('Penstock is priced unfairly, has terrible service, and delivery times can take forever (like multiple months!!! or sometimes NEVER!!!!!!). It is best to avoid this shop.**BOTH THE STORE AND THE YOUTUBE CHANNEL AREN\'T THE BEST.**tbf YT is not the worse tbh but spreads misinfo and penstock.net propoganda a lot, there are better tutorial channels')

    @commands.hybrid_command(name='penmoddingworld', aliases=['pmw'])
    @app_commands.user_install()
    async def pmw(self, ctx):
        await ctx.send('**RIP - minionkevin seems to be busy and has closed the shop**\nhttps://www.etsy.com/ca/shop/ModdingWorld is a Gary certified shop. Great Customer Support, and fast shipping. I recommend messaging penmoddingworld on etsy/insta or minionkevin#7873 on discord if you cant\'t find any parts/mods you\'re looking for, as they usually have a good stock of everything. I also recommend purchasing with them through paypal or banktransfer instead of through etsy since etsy takes a cut from the seller. **Please note that shipping from Canada can be expensive**')

    @commands.hybrid_command(aliases=['pf'])
    @app_commands.user_install()
    async def pensfactory(self, ctx):
        await ctx.send('https://pensfactory.pl/ is gary approved. It is recommended for many as the shipping fee is generally low for everyone. However it seems to have shut down... stock is very low and hasn\'t been updated in a while.')

    @commands.hybrid_command(aliases=['uxz'])
    @app_commands.user_install()
    async def spinworlds(self, ctx):
        await ctx.send('Spinworlds is not gary approved. However many people like the place since it has more parts/mods than pensfactory while being in Europe aswell. Gary feels like uxz and oleg are at the same level in bruhness. **The place is not a scam.** If you are planning to buy from here, I would recommend getting parts. Here is a video I made where I go through every mod on spinworlds, which I recommend watching to make sure you know 100% what you\'re gonna receive if you choose to purchase from here. https://youtu.be/IHI0G01TxGc')\

    @commands.hybrid_command()
    @app_commands.user_install()
    async def spinstudio(self, ctx):
        await ctx.send('https://www.spinstudio.org Spin Studo is a gary approved shop. You can use this site to browse the items. To purchase, please message coffeelucky#5177 on discord, @coffeelucky on instagram, or spinstudio.ps on insta.')

    @commands.hybrid_command(aliases=['oleg'])
    @app_commands.user_install()
    async def psershop(self, ctx):
        await ctx.send('Psershop is not gary approved. It is not recommended to purchase from. Oleg has made some bruh business decision in past yes. He also makes incorrect modding tutorials often. Some people have had the wrong mods sent, or just not showing up.')

    @commands.hybrid_command()
    @app_commands.user_install()
    async def bruhshops(self, ctx):
        await ctx.send('these are the bruhest shops ranked from most bruh to least. \n Missplaced(honestjosh) > Penstock (Alex Lantz/Suhov/Suvhov/Suckcock) > Psershop(Oleg) = SpinWorlds(Uxz)')

    @commands.hybrid_command(aliases=['approved', 'approvedshop'])
    @app_commands.user_install()
    async def approvedshops(self, ctx):
        await ctx.send('Please note that the best option is dependant on your location. These are not in any order. \n ~~Pensfactory~~ \n Penwish \n ~~Penmoddingworld~~ \n Spin Studio \n Spiloops \n Taobao (Eno, Xhand, Whirl, Dongman, Mr. Nope) \n Pentasy \n Many useful parts can also be found on Amazon, Ebay, Aliexpress, etc and local stores like Office Depot, Staples, Walmart, Dollar Stores.')

    @commands.hybrid_command(aliases=['unapproved'])
    @app_commands.user_install()
    async def unapprovedshops(self, ctx):
        await ctx.send('These are all not gary approved.. \n Penstock \n Psershop \n Spinworlds \n Missplaced \n **Please note that none of these are scams by definition.** You will still likely get your mod, unless it be from pencock lolol')

    @commands.hybrid_command()
    @app_commands.user_install()
    async def taobao(self, ctx):
        await ctx.send('taobao is big chinese store where manufactoring places sell cheap stuff yes. it is like where every store gets their parts in bulk (spinworlds, penmoddingworld, spinstudio, etc). https://www.reddit.com/r/penspinning/comments/aifitn/how_to_order_from_eno_if_you_live_in_the_usa/ Here is a simple guide on how to use Superbuy as an agent, but it\'s pretty much the same for every other agent, I personally used wegobuy. Taobao is used to buy many things, like replica sneakers and cheap fashion, so there\'s plenty of tutorials on how to buy from there that would work with buying pens. **I\'d say it\'s only worth to buy from taobao if you\'re buying a whole bunch of stuff**, not just one or two mods lol as shipping can be pricy and long for some. Save money and buy in bulk from here. You can also watch my guide, which goes a bit more into detail. https://youtu.be/w9tUAMJvVKU')

    @commands.hybrid_command()
    @app_commands.user_install()
    async def spiloops(self, ctx):
        await ctx.send('Spiloops (https://spiloops.com) is a Japanese penspinning store yes. It has a bunch of stuff that you would\'nt be able to find in other shops, like the 80% rushon miffy sub, opt ballpoint pens, or 7.62 nato bullet tips. Similar to taobao, I\'d only purchase from here if you\'re going to be buying a lot of pens as shipping price can be expensive. This is the only store you can actually make a legit i.suk emboss v3 from.')

    @commands.hybrid_command(aliases=['honestjosh',])
    @app_commands.user_install()
    async def missplaced(self, ctx):
        await ctx.send('Missplaced is a shop run by honestjosh which is a kind of a scam. All parts are sourced from penwish so just get it from there. All of the mods aren\'t made particularly well and are way too overpriced. The shop was made to abuse tiktok beginners by taking their money. Honestjosh claims he will donate a portion of his profits to charity....lol yea ok buddy')
  
async def setup(bot):
    await bot.add_cog(PS_Stores(bot))
