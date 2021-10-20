# Module to create points that consist
# of a city name,
# latitude and longtitude coordinates
from typing import Tuple


class Point:
    def __init__(self, name, latitude, longtitude) -> None:
        self._name = name
        self._longitude = longtitude
        self._latitude = latitude

    def get_lat_long(self) -> Tuple[int, int]:
        return (self._latitude, self._longitude)
