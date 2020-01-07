#!/usr/bin/python3
import json
from youtube_api import YoutubeApi

url_template = "https://www.youtube.com/user/{}/videos"

config = ''
def load_config():
    return json.load(open("config.json", "r"))

if __name__ == '__main__':
    config = load_config()
    yt = YoutubeApi(config['api_key'])

    for channel in config['channels']:
        url = url_template.format(channel['id'])
        yt.get_videos(url)
