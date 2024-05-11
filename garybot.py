import discord
import settings
from discord.ext import commands

client = commands.Bot(command_prefix = '>', intents = discord.Intents.all())

@client.event
async def on_ready():
    print('gary bot is  lets gooo')

@client.command()
async def modguide(ctx):
    await ctx.send('https://media.discordapp.net/attachments/833954424425545788/897172202942767194/unknown.png?width=382&height=300')

@client.command()
async def trickorder(ctx):
    await ctx.send('https://i.redd.it/wvax59fb41s11.png **This trick order is not gospel and a bit outdated.** I recommend just learning fundies in reverse and in all slots then learning whatever u want lol')

@client.command(aliases=['slomo'])
async def slowmo(ctx):
    await ctx.send('www.youtube.com')

@client.command(aliases=['penwish','pw'])
async def usa(ctx):
    await ctx.send('penwish.com is the recommended shop for american buyers, **international shipping be expensive so it aint the best if u no from usa**')

@client.command()
async def sls(ctx):
    await ctx.send('https://www.youtube.com/playlist?list=PLqvo4PPYx7nU8j3Cjz2u6dZ7s0FERNJ7y')

@client.command()
async def links1(ctx):
    await ctx.send('https://www.youtube.com/watch?v=4RZDt9B4sfQ')

@client.command()
async def links2(ctx):
    await ctx.send('https://www.youtube.com/watch?v=24CxVVMact4')

@client.command()
async def planet(ctx):
    await ctx.send('https://discord.gg/5thTVupNHh')

@client.command()
async def workshop(ctx):
    await ctx.send('https://discord.com/invite/7F4BjWD')

@client.command()
async def ipmc(ctx):
    await ctx.send('https://discord.gg/wby7U2g')
    
@client.command()
async def mpsd(ctx):
    await ctx.send('https://discord.gg/347xyYa')

@client.command()
async def reddit(ctx):
    await ctx.send('https://discord.com/invite/010bWcQCla9sRdYea')

@client.command()
async def penstock(ctx):
    await ctx.send('Penstock is priced unfairly, has terrible service, and delivery times can take forever (like multiple months!!! or sometimes NEVER!!!!!!). It is best to avoid this shop.**BOTH THE STORE AND THE YOUTUBE CHANNEL AREN\'T THE BEST.**tbf YT is not the worse tbh but spreads misinfo and penstock.net propoganda a lot, there are better tutorial channels')

@client.command()
async def psuk(ctx):
    await ctx.send('https://discord.gg/AE2WQrz5JM')

@client.command()
async def kronen(ctx):
    await ctx.send('https://discord.gg/AZDeABYj74')

@client.command(name='penmoddingworld', aliases=['pmw'])
async def pmw(ctx):
    await ctx.send('https://www.etsy.com/ca/shop/ModdingWorld is a Gary certified shop. Great Customer Support, and fast shipping. I recommend messaging penmoddingworld on etsy/insta or minionkevin#7873 on discord if you cant\'t find any parts/mods you\'re looking for, as they usually have a good stock of everything. I also recommend purchasing with them through paypal or banktransfer instead of through etsy since etsy takes a cut from the seller. **Please note that shipping from Canada can be expensive**')

@client.command()
async def cvs(ctx):
    await ctx.send('https://www.youtube.com/playlist?list=PLE4F7122D79474299 I recommend watching a bunch of cvs to get some inspiration! It\'s also a great way to develop spinning preferences and see potential areas you want to explore.')

@client.command(aliases=['notationbook', 'psbook',])
async def notation(ctx):
    await ctx.send('https://drive.google.com/file/d/1TlDb1H5bRnZZdswmdr07m-58yxs4Es7-/view Good Luck Studying for your AP Notation Test!')

@client.command(aliases=['pf'])
async def pensfactory(ctx):
    await ctx.send('https://pensfactory.pl/ is gary approved. It is recommended for many as the shipping fee is generally low for everyone. However it seems to have shut down... stock is very low and hasn\'t been updated in a while.')

@client.command(aliases=['uxz'])
async def spinworlds(ctx):
    await ctx.send('Spinworlds is not gary approved. However many people like the place since it has more parts/mods than pensfactory while being in Europe aswell. Gary feels like uxz and oleg are at the same level in bruhness. **The place is not a scam.** If you are planning to buy from here, I would recommend getting parts. Here is a video I made where I go through every mod on spinworlds, which I recommend watching to make sure you know 100% what you\'re gonna receive if you choose to purchase from here. https://youtu.be/IHI0G01TxGc')\

@client.command()
async def spinstudio(ctx):
    await ctx.send('https://www.spinstudio.org Spin Studo is a gary approved shop. You can use this site to browse the items. To purchase, please message coffeelucky#5177 on discord, @coffeelucky on instagram, or spinstudio.ps on insta.')

@client.command(aliases=['modtuts'])
async def pmpm(ctx):
    await ctx.send('https://penmodding.pm')

@client.command(aliases=['oleg'])
async def psershop(ctx):
    await ctx.send('Psershop is not gary approved. It is not recommended to purchase from. Oleg has made some bruh business decision in past yes. He also makes incorrect modding tutorials often. Some people have had the wrong mods sent, or just not showing up.')

@client.command()
async def bruhshops(ctx):
    await ctx.send('these are the bruhest shops ranked from most bruh to least. \n Missplaced(honestjosh) > Penstock (Alex Lantz/Suhov/Suvhov/Suckcock) > Psershop(Oleg) = SpinWorlds(Uxz)')

@client.command()
async def fenwiki(ctx):
    await ctx.send('https://wiki.fenspinner.net/index.php/Main_Page')

@client.command()
async def ogivan(ctx):
    await ctx.send('http://bbs.pserhome.com/archiver/?tid-44182.html')

@client.command(aliases=['beginnermod'])
async def beginnermods(ctx):
    await ctx.send('Beginner can spin whatever they want tbh. There are no mods specifically \'for beginners\', or \'for pros\', etc. We recommend ivan and hash comssa because they\'re cheap and easy to make.')
    
@client.command(aliases=['i.sukpapermod', 'isukpapermod'])
async def papermod(ctx):
    await ctx.send('https://youtu.be/y4jfJjyySQc')

@client.command()
async def waterfall(ctx):
    await ctx.send('Waterfall is a pretty meh mod. It has been recommended wayyyy too much over the years. It\'s honestly pretty mediocre for the price. People only want it because people have recommended it tbh, like when\'s the last time you seen waterfall in a cv bruh momento \nnormal waterfall > buster or comssa waterfall tho \nhalf dgg waterfall bestest tho')

@client.command(aliases=['flying_panda'])
async def flyingpanda(ctx):
    await ctx.send('Waterfall > Flying Panda. \nboth are pretty bad tho, not many still spin after experiencing other mods')

@client.command(aliases=['canadashops'])
async def canada(ctx):
    await ctx.send('For cheapest shipping, I would recommend shops and traders from Europe. Pensfactory.pl is suggested. Canada to Canada shipping is actually more expensive than EU to Canada oddly, so Penmoddingworld isn\'t the cheapest. Spinstudio is a good option aswell.')

@client.command(aliases=['approved', 'approvedshop'])
async def approvedshops(ctx):
    await ctx.send('Please note that the best option is dependant on your location. These are not in any order. \n Pensfactory \n Penwish \n Penmoddingworld \n Spin Studio \n Spiloops \n Taobao (Eno, Xhand, Whirl, Dongman, Mr. Nope) \n Pentasy \n Many useful parts can also be found on Amazon, Ebay, Aliexpress, etc and local stores like Office Depot, Staples, Walmart, Dollar Stores.')

@client.command(aliases=['unapproved'])
async def unapprovedshops(ctx):
    await ctx.send('These are all not gary approved.. \n Penstock \n Psershop \n Spinworlds \n Missplaced \n **Please note that none of these are scams by definition.** You will still likely get your mod, unless it be from pencock lolol')

@client.command(aliases=['sonic'])
async def sonictut(ctx):
    await ctx.send('https://youtu.be/IyfvQbepErw')

@client.command(aliases=['index'])
async def penindex(ctx):
    await ctx.send('https://docs.google.com/spreadsheets/d/1hcoKoxpsKErape9xDHWiMErspsXQS4bGGeomv4eP0K4/edit?usp=sharing')

@client.command(aliases=['bust', 'busttutorial'])
async def busttut(ctx):
    await ctx.send('These are gary approved bust tutorials. \n https://www.youtube.com/watch?v=TUYpVo14lWo \n https://www.youtube.com/watch?v=0yL7hn011V8&t \n https://www.youtube.com/watch?v=UvyNfif6Kdo')

@client.command()
async def modguide2(ctx):
    await ctx.send('https://media.discordapp.net/attachments/910992658036576296/922579145987342416/unknown.png')

@client.command(aliases=['g2', 'g2removal', 'g2grips'])
async def g2grip(ctx):
    await ctx.send('https://www.youtube.com/watch?v=HNZhY6q8Aw0')

@client.command(aliases=['walmartmod', 'walmart', 'walmartmodv1', 'garywalmartmod1', 'walmartmod1', ])
async def garywalmartmod(ctx):
    await ctx.send('https://www.youtube.com/watch?v=xJl72ZisCVw')

@client.command(aliases=["garybotfaq"])
async def garybot(ctx):
    await ctx.send('Gary bot was originally made for Gary\'s IT class. It was made to aid specifically the Penstock discord community. Due to the nicheness of Penspinning, the constant spreading of misleading information, and the likes of Alex Suhov.. more modern ideologies needed to be expressed to beginners. Additionally, penspinning is a little trickier to research information through google, most likely due to the unexpected shutdown of UPSB. With Gary Bot, one could answer a newbie\'s question without the need to type a whole ass paragraph, one could easily grab useful links without the hassle of searching through discord pins or browser bookmarks, and one could know what gary thinks on a specific topic. Be prepared for a lots of the bads of the grammar. **Gary Bot is very biased. It is meant as a 24/7 replacement for Gary and only spits out what Gary would say in certain situations.**')

@client.command(aliases=['ivanmod', 'ivan', 'ivanmodtut',])
async def ivantut(ctx):
    await ctx.send('https://wiki.fenspinner.net/index.php/Ivan_Mod \n You can also use Dr grip grips instead of airfit grips ')

@client.command(aliases=['hashcomssa',])
async def hashcomssatut(ctx):
    await ctx.send('https://penmodding.pm/archives/6978 \n **Please note that the modern hash comssa \(the one we are recommending\) uses comssa instead of Bellcolor and signo tips instead of hi tec c**')

@client.command()
async def plsmod(ctx):
    await ctx.send('**I highly recommend trying to mod.** We recommend ivan and hash comssa because they are cheap and easy to **MAKE**. Making simple mods is very very easy. If you\'re worried about cutting stuff, all you need is a boxcutter, or a razor blade, or a xacto knife, or just any sharp blade (you can buy xactos for like $1 bruh). Wrap tape along the grip/body and simply **cut along a line**. UNLESS YOU ARE ACTUALLY AN IDIOT, YOU WON\'T MESS UP. JUST MAKE SURE YOU KNOW WHAT UR DOING. If you somehow are uncapable of doing this, then I don\'t think you\'ll last in penspinning... THERE IS NO REASON NOT TO MOD EASY MODS EXCEPT THAT YOU\'RE LAZY. You gain modding knowledge, you gain access to literally ANY MOD rather than what shops sell. **You will also learn how to repurpose and modify mods to fit your preferences. Modding is also very fun. You will also learn how to create and design your own cool epic mod!!!!!** \n**WE LITTERALLY RECOMMEND IVAN AND HASH COMSSA BECAUSE THEY ARE EASY AF TO MAKE SO WHY TF WOULD YOU BUY IT PREMADE IDIOTS YOU MIGHT ASWELL BUY A HARDER MOD OR SMTH**')

@client.command(aliases=['ta', 'thumbaround',])
async def tatut(ctx):
    await ctx.send('https://raw.githubusercontent.com/M1zushi/pen-spinning-discord-bot/master/pics/ta_startingpos_by_Tombuto.jpg')

@client.command(aliases=['tarev', 'thumbaroundreverse', 'thumbaroundrev',])
async def tarevtut(ctx):
    await ctx.send('https://raw.githubusercontent.com/M1zushi/pen-spinning-discord-bot/master/pics/ta_rev_startingpos_by_Tombuto.jpg')

@client.command()
async def sex(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/910992658036576296/935422233160081488/unknown.png')

@client.command()
async def gay(ctx):
    await ctx.send('https://docs.google.com/document/d/13Pl82npI1GKLnZRA1GgPSFxj5I20u7k_T0Ypj3q7XjM/edit?usp=drivesdk')

@client.command()
async def retards(ctx):
    await ctx.send('the retard role is a throwback to the old penstock server where I would make a retard tier list to rank how annoying people were. **if you see somebody with this role, i would advise you to avoid listening to their advice**')

@client.command()
async def setup(ctx):
    await ctx.send('https://coffeeluckyps.wordpress.com/2021/10/19/camera-setup-guide-for-pen-spinning-combo/')

@client.command()
async def watchps(ctx):
    await ctx.send('It is recommended to watch penspinning content (not tiktok pls) to get inspiration, to develop a style preference, and stay motivated. This blog post by Hobby will help you get started. https://hobbylogics.tumblr.com/post/647667149683474432/getting-started-with-watching-pen-spinning-videos')

@client.command(aliases=['powerlearningorder', 'powerorder',])
async def powertrickorder(ctx):
    await ctx.send('http://isukps.blogspot.com/2017/01/power-trick-learning-and-difficulty.html')

@client.command()
async def webcams(ctx):
    await ctx.send('this some example of webcams that many popular spinners use. A cellphone works great too. http://penspipsnep.blog.fc2.com/blog-entry-23.html')

@client.command(aliases=['backaround', 'koreanbak', 'koreanback', 'back,', 'weissanback', 'weissback' 'koreanbak',])
async def bak(ctx):
    await ctx.send('bak = back = backaround = bakaround = korean bak \n KTRINH IS WRONG ABOUT THIS ONE TRUST ME ON THIS')

@client.command()
async def taobao(ctx):
    await ctx.send('taobao is big chinese store where manufactoring places sell cheap stuff yes. it is like where every store gets their parts in bulk \(spinworlds, penmoddingworld, spinstudio, etc\). https://www.reddit.com/r/penspinning/comments/aifitn/how_to_order_from_eno_if_you_live_in_the_usa/ Here is a simple guide on how to use Superbuy as an agent, but it\'s pretty much the same for every other agent, I personally used wegobuy. Taobao is used to buy many things, like replica sneakers and cheap fashion, so there\'s plenty of tutorials on how to buy from there that would work with buying pens. **I\'d say it\'s only worth to buy from taobao if you\'re buying a whole bunch of stuff**, not just one or two mods lol as shipping can be pricy and long for some. Save money and buy in bulk from here. You can also watch my guide, which goes a bit more into detail. https://youtu.be/w9tUAMJvVKU' )

@client.command()
async def spiloops(ctx):
    await ctx.send('Spiloops (https://spiloops.com) is a Japanese penspinning store yes. It has a bunch of stuff that you would\'nt be able to find in other shops, like the 80% rushon miffy sub, opt ballpoint pens, or 7.62 nato bullet tips. Similar to taobao, I\'d only purchase from here if you\'re going to be buying a lot of pens as shipping price can be expensive. This is the only store you can actually make a legit i.suk emboss v3 from.')

@client.command()
async def links3(ctx):
    await ctx.send('https://www.youtube.com/watch?v=sJjx797j1x8')
    
@client.command()
async def tornado(ctx):
    await ctx.send('Tornado is the japanese term for extended thumbaround (NOT CONTINUOUS). So please dont use the term tornado because: \n1. I highly doubt ur japanese, and even if u r then it would be silly for you to come here and assume everyone will contort to your tricknames, also japanese terms kinda wack so pls dont use them even if ur weeb\n2. ALEX SUHOV IS WRONG\n3. Naming this linkage is kinda bruh')

@client.command(aliases=['honestjosh',])
async def missplaced(ctx):
    await ctx.send('Missplaced is a shop run by honestjosh which is a kind of a scam. All parts are sourced from penwish so just get it from there. All of the mods aren\'t made particularly well and are way too overpriced. The shop was made to abuse tiktok beginners by taking their money. Honestjosh claims he will donate a portion of his profits to charity....lol yea ok buddy')
    
@client.command()
async def charge(ctx):
        await ctx.send('tbh this trick is fairly simple to understand from any tutorial off youtube, just keep practicing and trying. if ur really bad and taking 1 year to learn this then maybe send a video and ask what wrong\n**also its normal for the pen to move down when doing charge cont lol**')
        
@client.command()
async def links(ctx):
    await ctx.send('https://www.youtube.com/watch?v=4RZDt9B4sfQ\nhttps://www.youtube.com/watch?v=24CxVVMact4\nhttps://www.youtube.com/watch?v=sJjx797j1x8')
    
@client.command()
async def wenyu(ctx):
    await ctx.send('I believe Wenyu is the most proficient pen spinner in the history of pen spinning. His tunnel vision on refining the trick "fingerpass" is the most impressive display of  the greatness of the human mind. Not only is his sheer intelligence and dexterity compared to the likes of i.suk and Menowa* but also Einstein, Shakespeare, Picasso, and even Jesus himself. If you slow down his very impressive WR video you can see that in every pass his fingers dance as if they were cherry blossom petals flowing through the spring breeze. Each and every micrometer of movement in his fingers are calculated with quantum physics perfectly following the golden ratio. If we were to look inside his hands the blood would not be red, it would be gold. He has evolved to replace the cringe hemoglobin ridden blood of the ordinary human with Ichor, the blood of the Gods.  It is a miracle that he even permits our mortal human eyes to gaze upon his impeccably perfect fingerpass. Wenyu is truly a God amongst men.')
    
@client.command(aliases=['staplesmod', 'staples', 'staplesmodv1', 'garystaplesmod1', 'staplesmod1',])
async def garystaplesmod(ctx):
    await ctx.send('https://youtu.be/xgSxwK2zYpk')
    
@client.command()
async def spindys(ctx):
    await ctx.send('https://discord.gg/VzyYnfECnS')
    
@client.command()
async def fenspinner(ctx):
    await ctx.send('https://discord.gg/9ERAUCDAkS')

@client.command(aliases=['india'])
async def ibps(ctx):
	await ctx.send('https://discord.gg/tmFJMsbp7u')
    
@client.command(aliases=['guide','guide1','beginnerguide1'])
async def beginnerguide(ctx):
    await ctx.send('https://youtu.be/QUL49ntJwFM')
    
@client.command(aliases=['bestmod'])
async def bestpenmod(ctx):
    await ctx.send('There is no such things as a best pen mod. If there was, everybody would spin the same mod. Mods are entirely personal preference. While it could be said that there\'s some objectively better pen mods, do not let that prevent you from getting mods that you are personally interested in and want to make (please actually learn about more mods than ivan, menowa vgg, isuk emboss, ivan emboss, waterfall, flying panda, tornado, etc). **Every pen mod can be spun by any level**')
    
@client.command()
async def essentials(ctx):
    await ctx.send('This is playlist contains Gary\'s favourite penspinning videos and stuff he would recommend noobs watch aswell. https://youtube.com/playlist?list=PLkPBnIe5Br650sNllwRwlURZeBZDAjSrb')
    
@client.command()
async def chopstick(ctx):
    await ctx.send('https://youtu.be/9bAevHmu9oE')
    
@client.command()
async def drgrip(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/306632688721461248/1077824307679465533/image.png')
    
@client.command(aliases=['st'])
async def supertip(ctx):
    await ctx.send('https://youtu.be/ep6MSDCFHm0')
    
@client.command()
async def psworld(ctx):
    await ctx.send('https://discord.gg/74N96vrAdN')
    
client.run(settings.DISCORD_API_SECRET)
