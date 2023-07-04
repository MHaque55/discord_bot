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

birthdays = {"01/21": "Atif",
             "02/19": "Iram" ,
             "05/17": "Boro Vai",
             #"06/29": "Boro Vai",
             "06/08": "Dr. Numa",
             "07/06": "Dr. Rafeen",
             "08/07": "Sanaf",
             "09/08": "Sir Nafee",
             "10/01": "Prova Apu",
             "10/21": "Ahiyaaaaan",
             "11/08": "Siara",
             "11/18": "Sabeen",
             "11/30": "Afif Vai",
             "12/18": "Munimma"}

channel_id: str

@bot.event
async def on_ready():
    global channel_id
    guild_ct = 0

    print("Bot is online")

    for guild in bot.guilds:
        print(f'- {guild.id} (name: {guild.name})')
        guild_ct += 1
        if str(guild.name) == "Homies":
            channels = guild.channels

    print(f'{bot.user} is now running and in {guild_ct} servers')

    for ch in channels:
        #print(f'This channel\'s name {ch.name}')
        if str(ch.name) == "general":
            channel_id = ch.id
            print(f'found the channel {ch.name} and it\'s id {ch.id}')

    send_message.start()

@tasks.loop(seconds=60*60*24)
async def send_message():
    global birthdays, channel_id
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%m/%d")
    print(f'today is {formatted_date}')
    if formatted_date in birthdays:
        message = f'Today is {birthdays[formatted_date]}\'s birthday, don\'t forget to wish him/her'
        channel = bot.get_channel(int(channel_id))
        if channel:
            await channel.send(message)

# async def send_message_to_channel(message):
#     print()

bot.run(TOKEN)