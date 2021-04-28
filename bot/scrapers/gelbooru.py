from bot.scrapers.api import gelapi

#get api
from bot.config import gelbooru_api_key,gelbooru_user_id

# Add your gelbooru api

api_key = gelbooru_api_key
user_id = gelbooru_user_id


# Convert the input text into Api Format
def gelbooru(limit,tags):
    
    if len(tags) > 1:
        tags = tags.split(',')

    blacklisted = ['loli','guro'] #Enter Blacklisted tags here

    tags = "+".join(tags) + '+sort:random+-' + "+-".join(blacklisted)

    payload = {
        "api_key": api_key,
        "user_id": user_id,
        "page":"dapi",
        "s":"post",
        "q":"index",
        "limit":limit * 3,
        "tags":tags,
        "json":1 
    }  

    url = "https://gelbooru.com/index.php"
    
    return gelapi(url,payload,limit)  # Scrape Images From api

