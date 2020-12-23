# -*- coding: utf-8 -*-

import requests
import re
import json

from package.parser.parse_args import parse_args
from package.validator.check_args import check_args
from package.error.print_error import print_error
from package.cleaner.clean_url import clean_url
from package.getter.get_playlists import get_playlists
from package.getter.get_args_content import get_args_content
from package.init.init_data import init_data

def main():
    data = init_data(args)

    print(data.playlists)

    # init data 
    KEY = 'AIzaSyA-922kbGvt-VKYd4XIlEYXOqgxysY0gsI'
    url = 'https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10'
    url = clean_url(url)
 

    #for x in range(len(data.playlists)):
    #   print(data[x].playlists.name)
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
