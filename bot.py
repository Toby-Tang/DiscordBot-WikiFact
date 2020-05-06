# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from wikiparse_gen2 import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()
list_tables = table_compiler()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    good_commands = ['!factme', '!facme' ]
    bad_commands = ['!fuckme', '!fuckyou']
    good_response = ['FAC TIME BABY', 'FAC\'in right!', 'Hit\'ya with my best FAC!', 'Gimme a FAC\'in second!','FAC servers be slow today...','Yawn* What now? Ah FAC, right.']
    bad_response = ['!fuckyoutoo','!dontmakemefacu']

    if (message.content in good_commands):
        await message.channel.send(random.choice(good_response) + ' searchin\'...')
        p_title,p_comment,p_link = WikiFact(list_tables)
        await message.channel.send('**' + p_title + ':** ' + p_comment)
        await message.channel.send(p_link)

    if (message.content in bad_commands):
        await message.channel.send(random.choice(bad_response))
	
client.run(TOKEN)