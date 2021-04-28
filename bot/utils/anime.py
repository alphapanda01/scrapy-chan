import requests

def anime_reaction():
    url = requests.get("https://anime-reactions.uzairashraf.dev/api/reactions/random").json()['reaction']
    return url
