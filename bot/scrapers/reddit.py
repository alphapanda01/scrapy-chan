import praw
import requests
import bot.config as config

def leddit(site, msg):
    reddit = praw.Reddit(client_id=config.client_id,
                     client_secret = config.client_secret,
                     user_agent = config.user_agent,
                     check_for_async=False)
    
    subr = site
    sort = msg['tags']
    count = msg['limit']
   
    url = f'https://www.reddit.com/r/{subr}/'
    # To check if the subreddit exist
    check = requests.get(url).status_code

    print(check)

    if check == 404:
        return 0,0
    elif check == 502 or check == 200:
        try:
            subreddit = reddit.subreddit(subr)
            print(subreddit.title)
        except:
            return 0,0

        img = []
        i = 0

        if sort == 'top': 
            for submission in subreddit.top(limit=None):
                url = str(submission.url)

                if url.find('gfycat') != -1:
                    red = 'https://thumbs2.redgifs.com/{}.mp4'
                    name = url.split('/')[-1]
                    s_link = red.format(name)
                    img.append(s_link)
                    i+=1

                elif url.endswith('jpg') or url.endswith('jpeg') or url.endswith('gif') or url.endswith('png'):

                    img.append(url)
                    i += 1

                if i == count:
                    return list(img),2

        elif sort == 'hot': 
            for submission in subreddit.hot(limit=None):
                url = str(submission.url)

                if url.find('gfycat') != -1:
                    red = 'https://thumbs2.redgifs.com/{}.mp4'
                    name = url.split('/')[-1]
                    s_link = red.format(name)
                    img.append(s_link)
                    i+=1

                elif url.endswith('jpg') or url.endswith('jpeg') or url.endswith('gif') or url.endswith('png'):

                    img.append(url)
                    i += 1

                if i == count:
                    return list(img),2

        elif sort == 'new': 
            for submission in subreddit.new(limit=None):
                url = str(submission.url)

                if url.find('gfycat') != -1:
                    red = 'https://thumbs2.redgifs.com/{}.mp4'
                    name = url.split('/')[-1]
                    s_link = red.format(name)
                    img.append(s_link)
                    i+=1

                elif url.endswith('jpg') or url.endswith('jpeg') or url.endswith('gif') or url.endswith('png'):

                    img.append(url)
                    i += 1

                if i == count:
                    return list(img),2

        elif sort == 'rising': 
            for submission in subreddit.rising(limit=None):
                url = str(submission.url)


                if url.find('gfycat') != -1:
                    red = 'https://thumbs2.redgifs.com/{}.mp4'
                    name = url.split('/')[-1]
                    s_link = red.format(name)
                    img.append(s_link)
                    i+=1

                elif url.endswith('jpg') or url.endswith('jpeg') or url.endswith('gif') or url.endswith('png'):

                    img.append(url)
                    i += 1

                if i == count:
                    return list(img),2

        else:
            return 0,0

        
    else:
        return 0,0

'''
res codes 
    2 - success  # 2 is used to differentiate between normal sites and reddit
    0 - failed
'''
