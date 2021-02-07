import math


class MapParams:
    LAT_STEP = 0.008
    LON_STEP = 0.02

    def __init__(self):
        self.longitude = 65.332986
        self.latitude = 55.442192
        self.zoom = 15
        self.l_s = ['map', 'sat', 'sat,skl']
        self.l_index = 0
        self.points = []

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

    def set_pos(self, position):
        self.longitude = position[0]
        self.latitude = position[1]

    def add_point(self, point):
        self.points.append(point)

    def clear_points(self):
        self.points = []

    def get_points(self):
        return self.points

    def left(self):
        self.longitude -= self.LON_STEP * math.pow(2, 15 - self.zoom)

    def right(self):
        self.longitude += self.LON_STEP * math.pow(2, 15 - self.zoom)

    def up(self):
        self.latitude += self.LAT_STEP * math.pow(2, 15 - self.zoom)

    def down(self):
        self.latitude -= self.LAT_STEP * math.pow(2, 15 - self.zoom)

    def change_l(self):
        self.l_index += (1 if self.l_index != 2 else -2)

    def get_l(self):
        return self.l_s[self.l_index]

    def get_format(self):
        return 'PNG' if self.l_index == 0 else 'JPG'

    def set_address(self, text_edit, text):
        text_edit.setPlainText(text)

    def clear_address(self, text_edit):
        text_edit.setPlainText('')

    def reset_index(self, text_edit):
        text = text_edit.toPlainText()
        if 'Почтовый индекс:' in text:
            text_edit.setPlainText(text.split(' Почтовый индекс: ')[0])
        elif ' Почтового индекса нет' in text:
            text_edit.setPlainText(text.replace(' Почтового индекса нет', ''))