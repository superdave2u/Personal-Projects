#!/usr/bin/env python3

import requests
import json
import great_circle_calculator.great_circle_calculator as gcc


class hapiConnect():
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
        payload = {'lat': latitude, 'lon': longitude, 'maxDistance': maxDistance, 'maxResults': maxResults,
                   'sort': sort, 'minLength': minLength, 'minStars': minStars, 'key': self.key}
        r = requests.get('{}get-trails'.format(self.url), params=payload)

        return(r.text)

    def getTrailsById(self, ids):
        """[Returns trails for given IDs.]

        Args:
            ids ([str]): [one or more trail IDs, separated by commas]
        """
        payload = {'ids': ids, 'key': self.key}
        r = requests.get('{}get-trails-by-id?'.format(self.url), params=payload)

        return(r.text)

    def getConditions(self, ids):
        """[Returns conditions for a given trail.]

        Args:
            ids ([str]): [one or more trail IDs, separated by commas]
        """
        payload = {'ids': ids, 'key': self.key}
        r = requests.get('{}get-trails-by-id?'.format(self.url), params=payload).raise_for_status()

        return(r.text)


class gmapsConnect():
    def __init__(self, key):
        """[Google Maps API Connector]

        Args:
            key ([str]): [Google Maps API secret key]
        """
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        self.key = key

    def getLatLong(self, address):
        """[Returned in dict format, lat and long from a given address]

        Args:
            address ([str]): [The street address or plus code that you want to geocode.
            Specify addresses in accordance with the format used by the national postal
            service of the country concerned. Additional address elements such as business
            names and unit, suite or floor numbers should be avoided. Street address elements 
            should be delimited by spaces(shown here as url-escaped to %20): ]
        """
        payload = {'address': address, 'key': self.key}
        r = requests.get(self.url, params=payload)
        data = json.loads(r.text)
        return(data['results'][0]['geometry']['location'])


def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    return(gcc.distance_between_points((lon1, lat1), (lon2, lat2), unit='miles', haversine=True))


def midpoint(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle midpoint between two points
    on the earth (specified in decimal degrees)
    """
    lon, lat = gcc.midpoint((lon1, lat1), (lon2, lat2))
    return({'lat': lat, 'lon': lon})
