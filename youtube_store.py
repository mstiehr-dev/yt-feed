#!/usr/bin/python3

import json

class YoutubeStore:


    def __init__(self, path):
        # TODO: store backup of database file
        self.path = path
        self.data = json.load(open(self.path))

    def save(self):
        # TODO remove backup file
        json.dump(data, open(self.path, "w"))

    def update_channel(self, channel_id, incoming_videos):
        # TODO compare incoming videos with stored ones, return only unknown ones
        # TODO update storage
        return []


if __name__ == '__main__':
    YoutubeStore("db.json")
