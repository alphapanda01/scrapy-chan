# To parse messages for further usage

# msg should be in the str formate similar to this

# scrapy <site> <limit> <tags>


def parse(msg):
    
    try:
        _, site, limit, *tags = msg
    except:
        return 0,0,0 

    if len(tags) == 0:
        return 0,0,0
        

    if len(tags) < 1:
        tags = ['all']
    else:
        tags = tags[0]

    
    # fixing var `site`
    working_sites = ['gelbooru','konachan','rule34']

    if site.startswith('r/'):
        site = site[2:]
        if tags not in ['top', 'hot','new','rising']:
            tags = 'top'

    elif site not in working_sites:
        return 0,0,0

    # fixing var `limit`
    try:
        limit = int(limit)
    except:
        return 0,0,0

    # Do not put load on the api server
    if limit > 100:
        return 0,0,0



    data = { 
             'limit' : limit,
             'site' : site, 
             'tags' : tags, 
            }

    
    res = 1

    return site, data, res
