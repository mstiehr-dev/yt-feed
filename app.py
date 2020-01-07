#!/usr/bin/python3
import json

# url: https://www.youtube.com/user/globalmtb/videos

config = ''
def load_config():
    return json.load(open("config.json", "r"))

if __name__ == '__main__':
    config = load_config()
    for channel in config['channels']:
        print(channel['name'])
