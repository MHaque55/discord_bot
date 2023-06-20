import discord
import re
import requests
import os
import json

from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.guilds = True
intents.guild_messages = True
intents.emojis = True
intents.emojis_and_stickers = True
intents.reactions = True
intents.moderation = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print("Bot is online")
    guild_ct = 0
    for guild in bot.guilds:
        print(f'- {guild.id} (name: {guild.name})')
        guild_ct += 1
    print(f'{bot.user} is now running and in {guild_ct} servers')


TOKEN = "MTExOTg1Mjg1ODg1OTMzNTcxMg.G9lWmN.H4_6ciyxf_oXfar83e1uktlvveVakg4lFvTdZc"

bot.run(TOKEN)