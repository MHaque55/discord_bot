import discord
import datetime
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

bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = "MTEyMzAzNDAxNTY3OTY1NjEwNw.GHAhzl.HQ1TTa-5LGUme1KPYQKZmc3UnTKHgB8DdZOK8U"

birthdays = {"Atif": "",
             "Iram": "",
             "Navid": "",
             "Numa": "",
             "Rafeen": "",
             "Sanaf": "",
             "Nafee": "",
             "Prova": "",
             "Ahiyan": "",
             "Siara": "",
             "Sabeen": "",
             "Afif": "",
             "Munim": ""}

channel_id: str

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
        if str(ch.name) == "general":
            channel_id_skits = ch.id
            print(f'found the channel {ch.name} and it\'s id {ch.id}')

    send_message.start()

@tasks.loop(seconds=60)
async def send_message():
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%m/%d")
    print(f'today is {formatted_date}')


async def send_message_to_channel(message):
    print()

bot.run(TOKEN)