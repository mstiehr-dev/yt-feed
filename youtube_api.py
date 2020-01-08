#!/usr/bin/python3

import requests

class YoutubeApi(object):

    def __init__(self, api_key):
        self.api_key = api_key

    def get_videos(self, url):
        print(url)
        return []

    def get_channel_id(self, username):
        pass

# channel id ermitteln:
#url  "https://www.googleapis.com/youtube/v3/channels?part=id&key=<YOUR_KEY>&forUsername=leopardheadking&type=video"
'''
{
 "kind": "youtube#channelListResponse",
 "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/NeNwUGx--Ak1VYgmR8f_ZLLitzI\"",
 "pageInfo": {
  "totalResults": 1,
  "resultsPerPage": 5
 },
 "items": [
  {
   "kind": "youtube#channel",
   "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/Yf_8sQHhHx863zA_jHKxyBCnlCY\"",
   "id": "UC-WMwOzgFdvvGVLB1EZ-n-w"
  }
 ]
}
'''
# videoliste laden:
#curl  "https://www.googleapis.com/youtube/v3/search?part=snippet&key=<YOUR_KEY>&channelId=UC-WMwOzgFdvvGVLB1EZ-n-w"
'''
{
 "kind": "youtube#searchListResponse",
 "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/Z0J2UroBo3YzjOSuHDXHd8PtCXQ\"",
 "nextPageToken": "CAUQAA",
 "regionCode": "DE",
 "pageInfo": {
  "totalResults": 2930,
  "resultsPerPage": 5
 },
 "items": [
  {
   "kind": "youtube#searchResult",
   "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/Us0nPUmbQqDnRoRMODmtSlGGVyw\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "UQ-F6BGQH6A"
   },
   "snippet": {
    "publishedAt": "2018-12-04T19:00:03.000Z",
    "channelId": "UC-WMwOzgFdvvGVLB1EZ-n-w",
    "title": "CRAZY URBAN MTB DOWNHILL TRACK - FULL RACE RUN!",
    "description": "Here's my full race run down the crazy urban MTB downhill track in Medellin, Colombia! I love these urban mountain bike races because it is so sick to race ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/UQ-F6BGQH6A/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/UQ-F6BGQH6A/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/UQ-F6BGQH6A/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Sam Pilgrim",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/CPV_gyF5CE9-mV_34dUsSXFa4DQ\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "z-1QohLwe50"
   },
   "snippet": {
    "publishedAt": "2018-12-18T18:00:05.000Z",
    "channelId": "UC-WMwOzgFdvvGVLB1EZ-n-w",
    "title": "INSANE MEXICAN URBAN DOWNHILL - GoPro RACE RUN",
    "description": "This Insane Mexican urban downhill track through the streets of Taxco was so fun! This is my GoPro race run from the event. These mountain bike races through ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/z-1QohLwe50/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/z-1QohLwe50/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/z-1QohLwe50/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Sam Pilgrim",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/VOfZeMPRUjjjtFkTFXqsBifyRiY\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "e7HbLc-l8As"
   },
   "snippet": {
    "publishedAt": "2013-03-06T06:24:48.000Z",
    "channelId": "UC-WMwOzgFdvvGVLB1EZ-n-w",
    "title": "Sam Pilgrim - CALIFORNIA 2013",
    "description": "http://www.facebook.com/sampilgrimfanpage This is my newest edit from my annual trip to the USA. I like to come over to california in the off season to catch ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/e7HbLc-l8As/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/e7HbLc-l8As/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/e7HbLc-l8As/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Sam Pilgrim",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/e3ksFFNNvAVo7xtn5pWLxHreLO0\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "sYp8DFodzrs"
   },
   "snippet": {
    "publishedAt": "2019-05-21T17:00:08.000Z",
    "channelId": "UC-WMwOzgFdvvGVLB1EZ-n-w",
    "title": "INSANE URBAN MTB DOWNHILL IN MEXICO - FULL RACE RUN",
    "description": "My full speed race run from the insane urban MTB downhill in Mexico, through the streets of Puerto Vallarta with huge jumps, big drops and full speed stair ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/sYp8DFodzrs/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/sYp8DFodzrs/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/sYp8DFodzrs/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Sam Pilgrim",
    "liveBroadcastContent": "none"
   }
  },
  {
   "kind": "youtube#searchResult",
   "etag": "\"p4VTdlkQv3HQeTEaXgvLePAydmU/0SZBFH7edpAp9wS5wMtCw9_BmXM\"",
   "id": {
    "kind": "youtube#video",
    "videoId": "q79L_5UKv2Q"
   },
   "snippet": {
    "publishedAt": "2011-10-14T19:18:10.000Z",
    "channelId": "UC-WMwOzgFdvvGVLB1EZ-n-w",
    "title": "Sam pilgrim&#39;s HOW-TO. 360",
    "description": "So this is number three of my mountainbike HOW-TO series, This time im showing you the 360, once again it's just a lite tutorial an hopefully the slow motion and ...",
    "thumbnails": {
     "default": {
      "url": "https://i.ytimg.com/vi/q79L_5UKv2Q/default.jpg",
      "width": 120,
      "height": 90
     },
     "medium": {
      "url": "https://i.ytimg.com/vi/q79L_5UKv2Q/mqdefault.jpg",
      "width": 320,
      "height": 180
     },
     "high": {
      "url": "https://i.ytimg.com/vi/q79L_5UKv2Q/hqdefault.jpg",
      "width": 480,
      "height": 360
     }
    },
    "channelTitle": "Sam Pilgrim",
    "liveBroadcastContent": "none"
   }
  }
 ]
}
'''
