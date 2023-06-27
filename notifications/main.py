import discord
import scrapetube
#import instaloader 
import re


from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.guild_messages = True
intents.emojis = True
intents.emojis_and_stickers = True
intents.reactions = True
intents.moderation = True

TOKEN = "MTExOTg1Mjg1ODg1OTMzNTcxMg.G9lWmN.H4_6ciyxf_oXfar83e1uktlvveVakg4lFvTdZc"

latest_lbg = []
latest_442 = []
latest_beany = []
latest_ps = []
latest_caleb = []
latest_tifo = []
latest_angryjoe = []
#latest_fab_romano = []
#latest_livehwg = []

channel_id_skits: str
channel_id_sports: str
channel_id_gaming: str

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    global channel_id_skits, channel_id_sports, channel_id_gaming
    guild_ct = 0

    print("Bot is online")

    for guild in bot.guilds:
        print(f'- {guild.id} (name: {guild.name})')
        guild_ct += 1
        if str(guild.name) == "SamShed's server":
            channels = guild.channels

    print(f'{bot.user} is now running and in {guild_ct} servers')

    for ch in channels:
        #print(f'This channel\'s name {ch.name}')
        if str(ch.name) == "memes":
            channel_id_skits = ch.id
            print(f'found the channel {ch.name} and it\'s id {ch.id}')
            
        elif str(ch.name) == "sports":
            channel_id_sports = ch.id
            print(f'found the channel {ch.name} and it\'s id {ch.id}')

        elif str(ch.name) == "gaming-stuff":
            channel_id_gaming = ch.id
            print(f'found the channel {ch.name} and it\'s id {ch.id}')
        

    send_message.start()

@tasks.loop(seconds=120)
async def send_message():
    global latest_lbg, latest_caleb, latest_442, latest_ps, latest_beany,latest_tifo, latest_angryjoe
    #global latest_livehwg
    global channel_id_sports, channel_id_skits, channel_id_gaming
   
    
    videos_lbg = scrapetube.get_channel("UCWiY6fYdxuEe78r-0uFCnhA")
    videos_442 = scrapetube.get_channel("UC4SUUloEcrgjsxbmy_rQQXA")
    videos_beany = scrapetube.get_channel("UCiVg6vRhuyjsWgHkDNOig6A")
    videos_ps = scrapetube.get_channel("UC-2Y8dQb0S6DtpxNgAKoJKA")
    videos_caleb = scrapetube.get_channel("UCI1XS_GkLGDOgf8YLaaXNRA")
    videos_tifo = scrapetube.get_channel("UC6ZMmQaL9wZYo4iLw8n8xiA")
    videos_angryjoe = scrapetube.get_channel("UCsgv2QHkT2ljEixyulzOnUQ")
    
    #insta_bot = instaloader.Instaloader()
    #insta_fabr = instaloader.Profile.from_username(insta_bot.context, 'fabriziorom')
    #insta_livehwg= instaloader.Profile.from_username(insta_bot.context, 'liveherewego')


    for video in videos_lbg:
        if video['videoId'] not in latest_lbg:
            latest_lbg.append(video['videoId'])
            if len(latest_lbg) > 1:
                latest_lbg.pop(0)
            message = f"New LongBeachGriffy video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=LongBeachGriffy \n"
            await send_message_to_channel(message, channel_id_skits)
        break

    for video in videos_caleb:
        if video['videoId'] not in latest_caleb:
            latest_caleb.append(video['videoId'])
            if len(latest_caleb) > 1:
                latest_caleb.pop(0)
            message = f"New Calebcity video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=CalebCity \n"
            await send_message_to_channel(message, channel_id_skits)
        break
    
    for video in videos_442:
        if video['videoId'] not in latest_442:
            latest_442.append(video['videoId'])
            if len(latest_442) > 1:
                latest_442.pop(0)
            message = f"New 442oons video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=442oons \n"
            await send_message_to_channel(message, channel_id_skits)
        break

    for video in videos_beany:
        if video['videoId'] not in latest_beany:
            latest_beany.append(video['videoId'])
            if len(latest_beany) > 1:
                latest_beany.pop(0)
            message = f"New BeanymanSports video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=BeanymanSports \n"
            await send_message_to_channel(message, channel_id_sports)
        break

    for video in videos_tifo:
        if video['videoId'] not in latest_tifo:
            latest_tifo.append(video['videoId'])
            if len(latest_tifo) > 1:
                latest_tifo.pop(0)
            message = f"New Tifo IRL video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=TifoIRL \n"
            await send_message_to_channel(message, channel_id_sports)
        break

    for video in videos_ps:
        print(video['videoId'])
        print(f'latest ps: {latest_ps}')
        if video['videoId'] not in latest_ps:
            latest_ps.append(video['videoId'])
            print(f'latest ps after appending: {latest_ps}')
            if len(latest_ps) > 1:
                print("ps going here")
                latest_ps.pop(0)
                print(f'latest ps after popping: {latest_ps}')
            message = f"New Playstation video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=PlayStation \n"
            await send_message_to_channel(message, channel_id_gaming)
        break

    for video in videos_angryjoe:
        if video['videoId'] not in latest_angryjoe:
            latest_angryjoe.append(video['videoId'])
            if len(latest_angryjoe) > 1:
                latest_angryjoe.pop(0)
            message = f"New AngryJoeShow video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=AngryJoeShow \n"
            await send_message_to_channel(message, channel_id_gaming)
        break
        
    #for post in insta_fabr.get_posts():
     #     if len(latest_fab_romano) > 1:
      #          latest_fab_romano.pop(0)

       #     match = re.search(r'<Post\s+(\S+)>', str(post))
        #    if match:
         #       post_id = match.group(1)
          #      message = f"Fabrizio Romano\'s new post: https://www.instagram.com/p/{post_id}/?hl=en"
           #     await send_message_to_channel(message, channel_id_sports)
                
            #else:
             #   print("error")
                
        #break

    # for post in insta_livehwg.get_posts():
    #     if post not in latest_livehwg:
    #         latest_livehwg.append(post)
    #         if len(latest_livehwg) > 1:
    #             latest_livehwg.pop(0)

    #         match = re.search(r'<Post\s+(\S+)>', str(post))
    #         if match:
    #             post_id = match.group(1)
    #             message = f"Liveherewego posted something new: https://www.instagram.com/p/{post_id}/?hl=en"
    #             await send_message_to_channel(message, channel_id_sports)
    #         else:
    #             print("error")
    #     break


async def send_message_to_channel(message, channel_id):
    #global channel_id
    print("It's on")
    channel = bot.get_channel(int(channel_id))
    if channel:
        await channel.send(message)

bot.run(TOKEN)
