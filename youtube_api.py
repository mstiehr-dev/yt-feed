#!/usr/bin/python3

import requests

class YoutubeApi(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def get_videos(self, url):
        print(url)

    def get_channel_id(self, username):
        pass

# channel id ermitteln:
#url  "https://www.googleapis.com/youtube/v3/channels?part=snippet&key=AIzaSyB77ObzOPzctIsFdIgwaLsHhoSmYY_X8so&forUsername=leopardheadking&type=video"

# videoliste laden:
#curl  "https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyB77ObzOPzctIsFdIgwaLsHhoSmYY_X8so&channelId=UC-WMwOzgFdvvGVLB1EZ-n-w"
