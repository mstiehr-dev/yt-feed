#!/usr/bin/python3
import json
from collections import defaultdict
from youtube_api import YoutubeApi
from youtube_store import YoutubeStore

url_template = "https://www.youtube.com/user/{}/videos"
new_videos = dict()

config = ''
def load_config():
    return json.load(open("config.json", "r"))

def print_updates():
    for channel, videos in new_videos.items():
        # get channel name
        # get video title
        print(f"*** {channel} ")
        for video in videos:
            print(f"*** {video}") # todo extract title

        print("")

if __name__ == '__main__':
    config = load_config()
    yt = YoutubeApi(config['api_key'])
    db = YoutubeStore(config['database'])

    for channel in config['channels']:
        if 'id' in channel:
            id = channel['id']
            url = url_template.format(id)
            videos = yt.get_videos(url)
            new_videos[id] = db.update_channel(id, videos)
        else:
            print("need to get id for channel {}".format(channel['username']))

    print_updates()
