import requests

def gelapi(url,payload,limit):

    # ref - https://stackoverflow.com/questions/23496750/how-to-prevent-python-requests-from-percent-encoding-my-urls/23497912
    payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
    # Fixed unwanted URI encoding for tags

    # gets images from api
    try:
        r = requests.get(url,params=payload_str)
    except:
        #print("Error Occured, Unable to retrive data\nTry a Different tag combiantion or Wait for sometime before trying")
        return 0,0

    
    if r.status_code != 200:
        #print("Unable to Reach Website, Try again later")
        return 0,0

    #print(r.url)
    # converts into readable json

    try:
        jsonData = r.json()
    except:
        #print("Error Occured, Unable to retrive data\nTry a Different tag combiantion")
        return 0,0

    if len(jsonData) < 1:
        #print("No Images Found ;-;\nTry Searching Again")
        return 0,0
    elif len(jsonData) < limit:
        limit = len(jsonData)
        #print(f"Unable to find more then {len(jsonData)} images")

    # Get images images
    imgList = []
    for i in range(limit):
        imgList.append(jsonData[i]['file_url'])

    # print(imgList)
    
    result = 1

    return list(imgList),result


