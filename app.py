# -*- coding: utf-8 -*-

import discord
import logging
import sys # for logging into stdout

# helper/utility functions
from bot.utils.mparser import parse
from bot.utils.helper import helper_func
from bot.utils.anime import anime_reaction
import uwuify

# scraper function
from bot.scrapers.main import scrape

# apikey
from bot.config import API_KEY


client = discord.Client()

# Logging setup

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)

# stream handler
streamhandler = logging.StreamHandler(sys.stdout)
streamhandler.setLevel(logging.WARNING)
streamhandler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

#File handler
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))

logger.addHandler(handler)
logger.addHandler(streamhandler)

#####

@client.event
async def on_ready():
    login_msg = 'Logged in as {0.user}'.format(client)
    print(login_msg)
    logger.info(login_msg)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="hentai"))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    wigga = ['uwu','owo','awo','awu','uwy','chu','arigato','nya','chinchin']

    msgstr = str(message.content).lower()

    for i in wigga:
        if i in msgstr:
            flags = uwuify.SMILEY
            uwu = str(uwuify.uwu('!',flags=flags)).replace('!',"")
            await message.channel.send(uwu)

    msg = message.content


    if msg.startswith('scrapy') and len(msg.split()) > 1:

        msg = msg.split()

        if msg[1] == 'help':
            h = helper_func()
            await message.channel.send(h)
        
        elif msg[1] == 'react':
            url = anime_reaction()
            await message.channel.send(url)

        else:
            site, data, res = parse(msg)

            if not res:
                logger.warning("Failed parsing result.")
                logger.debug('reqby {0.author}, {0.content}'.format(message))
                await message.channel.send('Error\nPlease refer `scrapy help`')
            
            else:
                # WRITE LOGGER FOR THE DATA ASKED BY THE USER
                logger.info(f'{message.author}: {message.content}')
                result = 1
                # result = 1(success); 0(failed)
                lnks, result = scrape(site, data)
        
                if not result:
                    logger.warning(f'{message.content}: returned= {lnks}, res={result}')
                    await message.channel.send('Error\nPlease refer `scrapy help`')
                else: 
                    if result == 2:
                        for i in lnks:
                            await message.channel.send(i)
                    else:
                        for i in lnks[0]:
                            await message.channel.send(i)



client.run(API_KEY)
