import discord
import datetime
from discord.ext import commands
import re
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



bot = discord.Client(intents=intents)
bot2 = commands.Bot(command_prefix='!', intents=intents)

TOKEN = 'MTExMzEzMTY2NDQyMDM5MzAxMA.Ges2Nz.WRgvJta4FCc-cuBqTFG4xyYJqGzh4U118tHT7k'

#get the message id and guild id for the emoji role selector also the author
emo_msg_id = None
guild_id = None
@bot.event
async def on_ready():
    members = []
    guild_ct = 0
    for guild in bot.guilds:
        print(f'- {guild.id} (name: {guild.name})')
        guild_ct += 1

    for member in guild.members:
        print(f'the member: {member}')
        print()

    print(f'{bot.user} is now running and in {guild_ct} servers')

@bot.event
async def on_message(message):
    global emo_msg_id
    global guild_id
    guild_id = message.guild.id
    if message.author == bot.user:
        return
    #msg = msg.lower()
    
    print(f'{message.author} said "{message.content}" in {message.channel}')

   
    if isinstance(message.channel, discord.channel.DMChannel):
        await message.author.send(f'Okay I am a bot and have no clue what are you on. But I gotcha you said {message.content}')

    elif str(message.content) == "!role" and (str(message.channel) == "role-selection" or str(message.channel) == "just-for-bot-testing"):
        await message.channel.send("Choose the roles below")
        sent = await message.channel.send("```Not available for gaming? react with 💤\n\nAvailable for gaming? react with 🎮```")
        emo_msg_id = sent.id        #Getting the em_msg_id
        print(f'The message id {emo_msg_id}')
        
    elif str(message.channel) == "just-for-bot-testing":
        #print(f'the type of channel {type(message.channel)}')
        resp = response_server(message)
        await message.channel.send(resp)


@bot.event
async def on_raw_reaction_add(payload):
    global guild_id
    global emo_msg_id
    channel_id = payload.channel_id
    message_id = payload.message_id
    guild_id2 = payload.guild_id
    user_id = payload.user_id
    roles_emojis = {
        "🎮": "Pros",
        "💤": "Doesn't want to play"
    }

    print(f'{message_id} vs {emo_msg_id}')
    print(f'{guild_id2} vs {guild_id}')
    if guild_id2 == guild_id and message_id == emo_msg_id :  # Replace with your guild ID and message ID
        guild = bot.get_guild(guild_id)
        channel = guild.get_channel(channel_id)
        message = await channel.fetch_message(message_id)
        user = guild.get_member(user_id)
        if user is None:
            user = await guild.fetch_member(payload.user_id)


        print(f'the guild: {guild}\nchannel: {channel}\nmessage: {message}\nuser:{user}')
        
        emoji = payload.emoji.name

        if emoji == "💤":
            role_name = 'Doesn\'t want to play'
            role = discord.utils.get(guild.roles, name='Doesn\'t want to play')
            print("You are lazy")
        elif emoji == "🎮":
            role_name = 'Pros'
            role = discord.utils.get(guild.roles, name='Pros')
            print("Let's gooooo")
        else:
            print("Alright but not the right emoji")

        if role is not None:
            await user.add_roles(role)
            print(f"Assigned role '{role_name}' to {user.display_name}")
            print(f'{user.roles}')
            for current_role in user.roles:
                print(f'current role = {current_role} and role = {role}')
                if str(role) == "Pros" and str(current_role) == "Doesn\'t want to play":
                    print(f'current role under if = {current_role}')
                    await user.remove_roles(current_role)
                    print(f"{user.display_name} left {current_role}")

                elif str(role) == "Doesn\'t want to play" and str(current_role) == "Pros":
                    print(f'current role under if = {current_role}')
                    await user.remove_roles(current_role)
                    print(f"{user.display_name} left {current_role}")

@bot.event
async def on_raw_reaction_remove(payload): 
    global guild_idls
    channel_id = payload.channel_id
    message_id = payload.message_id
    guild_id2 = payload.guild_id
    user_id = payload.user_id
    roles_emojis = {
        "🎮": "Pros",
        "💤": "Doesn't want to play"
    }

    print(f'{message_id} vs {emo_msg_id}')
    print(f'{guild_id2} vs {guild_id}')
    if guild_id2 == guild_id and message_id == emo_msg_id :  # Replace with your guild ID and message ID
        guild = bot.get_guild(guild_id)
        channel = guild.get_channel(channel_id)
        message = await channel.fetch_message(message_id)
        user = guild.get_member(user_id)
        if user is None:
            user = await guild.fetch_member(payload.user_id)

        print(f'the guild: {guild}\nchannel: {channel}\nmessage: {message}\nuser:{user}')
        
        emoji = payload.emoji.name

        if emoji == "💤":
            role_name = 'Doesn\'t want to play'
            role = discord.utils.get(guild.roles, name='Doesn\'t want to play')
            print("You are lazy")
        elif emoji == "🎮":
            role_name = 'Pros'
            role = discord.utils.get(guild.roles, name='Pros')
            print("Let's gooooo")
        else:
            print("Alright but not the right emoji")

        if role is not None:
            await user.remove_roles(role)
            print(f"removed role '{role_name}' from {user.display_name}")

#Helper channel, for responding to messages in server
def response_server(message):
    message_lowercase = str(message.content).lower()
    if message_lowercase == "time":
        current_datetime = datetime.datetime.now()
        formatted_time = current_datetime.strftime("%I:%M:%S %p")
        return f'Right now it is {formatted_time}'
    
    elif message_lowercase == "date":
        current_datetime = datetime.datetime.now()
        formatted_date = current_datetime.strftime("%Y-%m-%d")
        return f'Today it is {formatted_date}'
    
    elif message_lowercase == "hello bot" or str(message.content).lower() == "hi bot":
        return f'Hey there how can I help you today?'
    
    else:
        return f'I am at my limit'
    
    
bot.run(TOKEN)
