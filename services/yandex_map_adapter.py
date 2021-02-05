from services.i_map_service import IMapService
import requests


class YandexMapAdapter(IMapService):
    map_request = "http://static-maps.yandex.ru/1.x/"

    def get_map(self, longitude, latitude, zoom, map):
        return requests.get(self.map_request,params={'ll': str(longitude) + ',' + str(latitude),
                                                     'z': zoom,
                                                     'l': map}).content
