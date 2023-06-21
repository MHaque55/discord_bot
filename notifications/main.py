import discord
import re
import requests
import os
import json
import scrapetube

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
latest_espn = []
latest_ps = []
channel_id: str

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.event
async def on_ready():
    global channel_id
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
        if str(ch.name) == "notify_content":
            channel_id = ch.id
            print(f'found the channel {ch.name} and it\'s id {ch.id}')
            break

    send_message.start()

@tasks.loop(seconds=120)
async def send_message():
    global latest_lbg, latest_espn, latest_442, latest_ps
    global channel_id
    videos_lbg = scrapetube.get_channel("UCWiY6fYdxuEe78r-0uFCnhA")
    videos_442 = scrapetube.get_channel("UC4SUUloEcrgjsxbmy_rQQXA")
    videos_espn = scrapetube.get_channel("UC6c1z7bA__85CIWZ_jpCK-Q")
    videos_ps = scrapetube.get_channel("UC-2Y8dQb0S6DtpxNgAKoJKA")
    
    for video in videos_lbg:
        if video['videoId'] not in latest_lbg:
            latest_lbg.append(video['videoId'])
            if len(latest_lbg) > 1:
                latest_lbg.pop(0)
            message = f"New LongBeachGriffy video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=LongBeachGriffy \n"
            await send_message_to_channel(message)
        break

    for video in videos_442:
        if video['videoId'] not in latest_442:
            latest_442.append(video['videoId'])
            if len(latest_442) > 1:
                latest_442.pop(0)
            message = f"New 442oons video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=442oons \n"
            await send_message_to_channel(message)
        break

    for video in videos_espn:
        if video['videoId'] not in latest_espn:
            latest_espn.append(video['videoId'])
            if len(latest_espn) > 1:
                latest_espn.pop(0)
            message = f"New ESPN_FC video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=ESPNFC \n"
            await send_message_to_channel(message)
        break

    for video in videos_ps:
        if video['videoId'] not in latest_ps:
            latest_ps.append(video['videoId'])
            if len(latest_ps) > 1:
                latest_ps.pop(0)
            message = f"New Playstation video:\nhttps://www.youtube.com/watch?v={video['videoId']}&ab_channel=PlayStation \n"
            await send_message_to_channel(message)
        break


    
async def send_message_to_channel(message):
    global channel_id
    print("It's on")
    channel = bot.get_channel(int(channel_id))
    if channel:
        await channel.send(message)


bot.run(TOKEN)