# Please add your bot api key here

#######

import os

disc = os.environ.get('API_KEY')

if disc:
    API_KEY = disc
else:
    print("Please Setup Discord Api")
    API_KEY = '{DISCORD_API_KEY_HERE}'
    # Setup the above key if hosting maually


#reddit

cli_id = os.environ.get("client_id")
cli_sec = os.environ.get('client_secret')

if cli_id and cli_sec:
    client_id = cli_id
    cli_secret = cli_sec
else:
    print("Please Set up Redit api ")
    client_id = "{REDDIT_CLIENT_ID}"
    client_secret = "{REDDIT_CLIENT_SECRET}"
    # Setup the above key if hosting maually

user_agent = 'scrapy'


# Gelbooru.com api
## This is optional
gelbooru_api_key = 'anonymous'
gelbooru_user_id = '9455'
