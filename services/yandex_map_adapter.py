from services.i_map_service import IMapService
import requests


class YandexMapAdapter(IMapService):
    map_request = "http://static-maps.yandex.ru/1.x/"
    geocode_request = 'http://geocode-maps.yandex.ru/1.x/'

    def get_map(self, longitude, latitude, zoom, map, points):
        params = {'ll': str(longitude) + ',' + str(latitude),
                  'z': zoom,
                  'l': map}
        if points:
            params['pt'] = '~'.join([','.join([str(i) for i in point_pos]) for point_pos in points])
        return requests.get(self.map_request, params=params).content

    def search_pos(self, search_line):
        response = requests.get(self.geocode_request, params={'geocode': search_line,
                                                              'apikey': "40d1649f-0493-4b70-98ba-98533de7710b",
                                                              'format': 'json'}).json()
        # return response
        return list(map(float, response['response']['GeoObjectCollection'][
            'featureMember'][0]['GeoObject']['Point']['pos'].split()))
