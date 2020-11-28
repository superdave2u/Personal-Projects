#!/usr/bin/env python3

import requests


class connect():
    def __init__(self, key):
        """[Constructor for the connection]

        Args:
            key ([str]): [www.hikingproject.com/data]
        """
        self.url = 'https://www.hikingproject.com/data/'
        self.key = key

    def getTrails(self, latitude, longitude, maxDistance=30, maxResults=10, sort='quality', minLength=0, minStars=0):
        """[Returns trails for a given query.]

        Args:
            latitude ([str]): [Latitude for a given area]
            longitude ([str]): [Longitude for a given area]
            maxDistance (int, optional): [Max distance, in miles, from lat, lon, Max: 200]. Defaults to 30.
            maxResults (int, optional): [Max number of trails to return. Max: 500]. Defaults to 10.
            sort (str, optional): [Values can be 'quality', 'distance']. Defaults to 'quality'.
            minLength (int, optional): [Min trail length, in miles]. Defaults to 0.
            minStars (int, optional): [Min star rating, 0-4]. Defaults to 0.
        """
        r = requests.get(
            '{}get-trails?lat={}?&lon={}&maxDistance={}&maxResults={}&sort={}&minLength={}&minStars={}&key={}'.format(
                self.url, latitude, longitude, maxDistance, maxResults, sort, minLength, minStars, self.key)
            ).raise_for_status()
        return(r.json)

    def getTrailsById(self, ids):
        """[Returns trails for given IDs.]

        Args:
            ids ([str]): [one or more trail IDs, separated by commas]
        """
        r = requests.get(
            '{}get-trails-by-id?ids={}&key={}'.format(self.url, ids, self.key)
        ).raise_for_status()
        return(r.json)

    def getConditions(self, ids):
        """[Returns conditions for a given trail.]

        Args:
            ids ([str]): [one or more trail IDs, separated by commas]
        """
        r = requests.get(
            '{}get-trails-by-id?ids={}&key={}'.format(self.url, ids, self.key)
        ).raise_for_status()
        return(r.json)
