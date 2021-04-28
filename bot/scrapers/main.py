from bot.scrapers.gelbooru import gelbooru
from bot.scrapers.konachan import konachan
from bot.scrapers.rule34 import rule34 
from bot.scrapers.reddit import leddit 



def scrape(site, data):

    if site == 'gelbooru':
        *links, result = gelbooru(data['limit'], data['tags'])
    elif site == 'konachan':
        *links, result = konachan(data['limit'], data['tags'])
    elif site == 'rule34':
        *links, result = rule34(data['limit'], data['tags'])
    else:
        if data['tags'] in ['top','hot','new','rising']:
            links , result = leddit(site, data)
        else:
            return 0,0

    return links,result
