# This example uses the geolib library:
# https://pypi.org/project/geolib/

"""
>>> shanghai = 31.2304, 121.4737
>>> geohash(shanghai)
'wtw3sjq6q'
"""

from geolib import geohash as gh

PRECISION = 9


def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)
