import requests, json

def getReddit():
    try:
        request = requests.get(f'https://www.reddit.com/r/gaming/top.json?limit=1&t=day', headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()

def getPostTitles(redditdata):
    posts = []
    for post in redditdata['data']['children']:
        x = post['data']['title']
        posts.append(x)
    return posts

def getResults(redditdata):
    myDict = {}
    for post in redditdata['data']['children']:
        rtitle = post['data']['title']
        rurl = post['data']['url']
    return (rtitle, rurl)

def getRedditData():
    redditdata = getReddit()
    (title, url) = getResults(redditdata)
    return (title, url)
