# -*- coding: utf-8 -*-

import requests
import re

from package.parser.parse_args import parse_args
from package.validator.check_args import check_args

def get_playlist():

#read file
    return playlists
def init_data():
    class Data:
        def __init__(self, lang, playlists):
            self.lang = lang, 
            self.playlists = playlists
    
    data = Data('fr', get_playlists())
    return data

def main():


    if check_args(args) is False:
        init_data()    
    print(args.url)
    
    # init data 
    KEY = 'AIzaSyA-922kbGvt-VKYd4XIlEYXOqgxysY0gsI'
    url = 'https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10'
    url = re.search('list=(.*?)$', url).group(1)
 
    """
    r = requests.get('https://www.googleapis.com/youtube/v3/playlists/', params = {
        'part': 'snippet',
        'maxResults': 5,
        'key': KEY,
        'id': url
    })

    data = r.json()

    print(data)
    """

if __name__ == '__main__':
    args = parse_args()
    main()
