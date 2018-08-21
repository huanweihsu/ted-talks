### A script to generate a list of YouTube links from TEDTalk ###

# Import require module #
import requests
import sys
import urllib
from bs4 import BeautifulSoup

# This function loads urls in a txt file,
# then transforms into YouTube links
def Load_url(filename):
    url_list = []
    youtube = 'https://www.youtube.com'
    youtube_search = 'https://www.youtube.com/results?search_query='
    # Load urls in the file
    with open(filename, 'r') as f:
        for i in f:
            # Videos from ted.com
            if 'ted' in i:
                # Extract title of the video
                query = i.split('/')[-1].split('\n')[0].split('?')[0]
                query = query.replace('_',' ')
                try:
                    query = urllib.quote(query)
                except:
                    query = urllib.parse.quote(query)
                # Search the video on YouTube
                r = requests.get(youtube_search+query)
                soup = BeautifulSoup(r.content,'html.parser')
                # Save the first result
                for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                    if 'watch?v' in vid['href']:
                        print('https://www.youtube.com' + vid['href'])
                        url_list.append(youtube+vid['href'])
                        break
            # Videos from YouTube
            elif 'youtu' in i:
                url_list.append(i)
            else:
                continue
    return url_list

if len(sys.argv) < 2:
    sys.exit('Require a file, usage: python crawler.py url.txt')
ul = Load_url(sys.argv[1])
with open('youtubelist.txt', 'w') as f:
    for i in ul:
        f.write(i)
