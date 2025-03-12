import discord
import settings
from discord.ext import commands

client = commands.Bot(command_prefix = '>', intents = discord.Intents.all())

@client.event
async def on_ready():
    print('gary bot is lets gooo')

    for cog_file in settings.COGS_DIR.glob("*.py"):
        if cog_file!= "__init__.py":
            await client.load_extension(f"cogs.{cog_file.name[:-3]}")

@client.event
async def on_command_error(ctx, error):
    '''
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("bruh :woman_zombie:")
    '''
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.add_reaction('🧟‍♀️')

   #add more errors here later...

@client.command()
async def modguide(ctx):
    await ctx.send("https://media.discordapp.net/attachments/833954424425545788/897172202942767194/unknown.png?width=382&height=300\n" +
                   "There\'s also a bunch of really underrated and accessible mods that you can make with parts you can get nearby. " + 
                   "Please talk with modders from your country to learn about them!")

@client.command()
async def trickorder(ctx):
    await ctx.send('https://i.redd.it/wvax59fb41s11.png **This trick order is not gospel and a bit outdated.** I recommend just learning fundies in reverse and in all slots then learning whatever u want lol')

@client.command(aliases=['slomo'])
async def slowmo(ctx):
    await ctx.send('www.youtube.com\njust change playback to 0.25 or whatever and hope there\'s enough frames lmao')

@client.command(aliases=['penwish','pw'])
async def usa(ctx):
    await ctx.send('penwish.com is the recommended shop for american buyers, **international shipping be expensive so it aint the best if u no from usa**')

@client.command(aliases=['notationbook', 'psbook', 'book'])
async def notation(ctx):
    await ctx.send('https://drive.google.com/file/d/1TlDb1H5bRnZZdswmdr07m-58yxs4Es7-/view Good Luck Studying for your AP Notation Test!')

@client.command(aliases=['modtuts'])
async def pmpm(ctx):
    await ctx.send('https://penmodding.pm')

@client.command()
async def fenwiki(ctx):
    await ctx.send('https://wiki.fenspinner.net/index.php/Main_Page')

@client.command()
async def ogivan(ctx):
    await ctx.send('http://bbs.pserhome.com/archiver/?tid-44182.html')

@client.command(aliases=['beginnermod'])
async def beginnermods(ctx):
    await ctx.send("Beginner can spin whatever they want tbh. There are no mods specifically " +
                "\"for beginners\", or \"for pros\", etc. We recommend ivan and hash comssa " +
                   "because they\'re cheap and easy to make. I would just recommend anything cheap and accessible " +
                   "to you, eg. for me that would be gary walmart/staples mod, xeran st, shoelotion waterfall, mango sharpie " +
                   "tul, etc")
    
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

@client.command(aliases=['index'])
async def penindex(ctx):
    await ctx.send('https://docs.google.com/spreadsheets/d/1hcoKoxpsKErape9xDHWiMErspsXQS4bGGeomv4eP0K4/edit?usp=sharing')

@client.command()
async def modguide2(ctx):
    await ctx.send('https://media.discordapp.net/attachments/910992658036576296/922579145987342416/unknown.png')

client.command(aliases=["garybotfaq"])
async def garybot(ctx):
    await ctx.send('Gary bot was originally made for Gary\'s IT class. It was made to aid specifically the Penstock discord community. Due to the nicheness of Penspinning, the constant spreading of misleading information, and the likes of Alex Suhov.. more modern ideologies needed to be expressed to beginners. Additionally, penspinning is a little trickier to research information through google, most likely due to the unexpected shutdown of UPSB. With Gary Bot, one could answer a newbie\'s question without the need to type a whole ass paragraph, one could easily grab useful links without the hassle of searching through discord pins or browser bookmarks, and one could know what gary thinks on a specific topic. Be prepared for a lots of the bads of the grammar. **Gary Bot is very biased. It is meant as a 24/7 replacement for Gary and only spits out what Gary would say in certain situations.**')

@client.command(aliases=['ivanmod', 'ivan', 'ivanmodtut',])
async def ivantut(ctx):
    await ctx.send('https://wiki.fenspinner.net/index.php/Ivan_Mod \n You can also use Dr grip grips instead of airfit grips ')

@client.command(aliases=['hashcomssa',])
async def hashcomssatut(ctx):
    await ctx.send('https://penmodding.pm/archives/6978 \n **Please note that the modern hash comssa (the one we are recommending) uses comssa instead of Bellcolor and signo tips instead of hi tec c**')

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
async def tornado(ctx):
    await ctx.send('Tornado is the japanese term for extended thumbaround (NOT CONTINUOUS). So please dont use the term tornado because: \n1. I highly doubt ur japanese, and even if u r then it would be silly for you to come here and assume everyone will contort to your tricknames, also japanese terms kinda wack so pls dont use them even if ur weeb\n2. ALEX SUHOV IS WRONG\n3. Naming this linkage is kinda bruh')
   
@client.command()
async def charge(ctx):
        await ctx.send('tbh this trick is fairly simple to understand from any tutorial off youtube, just keep practicing and trying. if ur really bad and taking 1 year to learn this then maybe send a video and ask what wrong\n**also its normal for the pen to move down when doing charge cont lol**')
        
@client.command()
async def wenyu(ctx):
    await ctx.send('I believe Wenyu is the most proficient pen spinner in the history of pen spinning. His tunnel vision on refining the trick "fingerpass" is the most impressive display of  the greatness of the human mind. Not only is his sheer intelligence and dexterity compared to the likes of i.suk and Menowa* but also Einstein, Shakespeare, Picasso, and even Jesus himself. If you slow down his very impressive WR video you can see that in every pass his fingers dance as if they were cherry blossom petals flowing through the spring breeze. Each and every micrometer of movement in his fingers are calculated with quantum physics perfectly following the golden ratio. If we were to look inside his hands the blood would not be red, it would be gold. He has evolved to replace the cringe hemoglobin ridden blood of the ordinary human with Ichor, the blood of the Gods.  It is a miracle that he even permits our mortal human eyes to gaze upon his impeccably perfect fingerpass. Wenyu is truly a God amongst men.')
    
@client.command(aliases=['bestmod'])
async def bestpenmod(ctx):
    await ctx.send('There is no such things as a best pen mod. If there was, everybody would spin the same mod. Mods are entirely personal preference. While it could be said that there\'s some objectively better pen mods, do not let that prevent you from getting mods that you are personally interested in and want to make (please actually learn about more mods than ivan, menowa vgg, isuk emboss, ivan emboss, waterfall, flying panda, tornado, etc). **Every pen mod can be spun by any level**')
    
@client.command()
async def drgrip(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/306632688721461248/1077824307679465533/image.png')

@client.command()
async def stdiff(ctx):
    await ctx.send('https://www.instagram.com/p/BtXJNG7Bqaq/?img_index=1')

'''
@client.command()
async def ping(ctx):
    await ctx.message.author.send("bro.. aint no way u be pinging a robot LMAO")
'''
    
    
client.run(settings.DISCORD_API_SECRET)
