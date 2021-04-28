from random import randint
from bot.scrapers.api import gelapi

def rule34(limit,tags):

    rand = 'score:>='+str(randint(0,200)) # To get random images with help of score
    
    if len(tags) > 1:
        tags = tags.split(',')
    
    blacklisted = ['loli*','guro*','furry*'] # Enter Blacklisted tags here
    
    tags = "+".join(tags) + '+' + rand + '+-' + "+-".join(blacklisted) 

    payload = {
        "page":"dapi",
        "s":"post",
        "q":"index",
        "limit":limit * 10,
        "tags":tags,
        "json":1 
        }

    url = "https://rule34.xxx/index.php"

    return gelapi(url,payload,limit)


