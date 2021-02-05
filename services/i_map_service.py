from abc import ABC, abstractmethod


class IMapService(ABC):
    @abstractmethod
    def get_map(self, longitude, latitude, zoom, map, points):
        pass

    @abstractmethod
    def search_pos(self, search_line):
        pass

