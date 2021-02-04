from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication

from application_service.get_map_uc import GetMapUseCase
from domain.map_params import MapParams


class MainWindow(QWidget):
    def __init__(self, uc: GetMapUseCase, parent=None):
        super().__init__(parent)

        self.map_label = QLabel(self)

        layout = QVBoxLayout()
        layout.addWidget(self.map_label)

        self.setLayout(layout)

        self.uc = uc

        self.show_map()

    def show_map(self):
        map_params = MapParams()
        map = self.uc.execute(map_params)

        pixmap = QPixmap()
        pixmap.loadFromData(map, 'PNG')
        self.map_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()
