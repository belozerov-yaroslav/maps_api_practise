class MapParams:
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