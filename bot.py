# ===========================================================
# NAME: Wikipedia Unusual Articles- bot.py
# BY: Toby Tang 
# Last Update: MAY 14, 2020
#
# Integrates discord interface with webscrapping code. Once
# the bot is added to a server, command '!factme' will return
# a random Wikipedia Unusual Articles page article.
# 
# Discord bot link: https://top.gg/bot/704890634984751126
# Github: https://github.com/Toby-Tang/DiscordBot-WikiFact
# ===========================================================
import os
import random
import discord
from dotenv import load_dotenv
from wikiparse_gen2 import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()
list_articles = article_compiler()

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
    
    if message.author.bot:
        return

    good_commands = ['!factme']
    good_response = ['FACT TIME BABY', 'Hit\'ya with my best FACT!', 'Gimme a second!','FACT servers be slow today...','Yawn* What now? Ah FACT, right.']

    if (message.content in good_commands):
        await message.channel.send(random.choice(good_response) + ' searchin\'...')
        p_title,p_comment,p_link = WikiFact(list_articles)
        await message.channel.send('**' + p_title + ':** ' + p_comment)
        await message.channel.send(p_link)
	
client.run(TOKEN)
