import math


class MapParams:
    LAT_STEP = 0.008
    LON_STEP = 0.02

    def __init__(self):
        self.longitude = 65.332986
        self.latitude = 55.442192
        self.zoom = 15

    def up_zoom(self):
        self.zoom += 1

    def down_zoom(self):
        self.zoom -= 1

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_zoom(self):
        return self.zoom

    def left(self):
        self.longitude -= self.LON_STEP * math.pow(2, 15 - self.zoom)

    def right(self):
        self.longitude += self.LON_STEP * math.pow(2, 15 - self.zoom)

    def up(self):
        self.latitude += self.LAT_STEP * math.pow(2, 15 - self.zoom)

    def down(self):
        self.latitude -= self.LAT_STEP * math.pow(2, 15 - self.zoom)