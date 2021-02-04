from PyQt5 import QtGui
from PyQt5.QtCore import Qt
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

        self.map_params = MapParams()

        self.show_map()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        key = event.key()
        if key == Qt.Key_PageUp:
            self.map_params.up_zoom()
        elif key == Qt.Key_PageDown:
            self.map_params.down_zoom()
        elif key == Qt.Key_Up:
            self.map_params.up()
        elif key == Qt.Key_Down:
            self.map_params.down()
        elif key == Qt.Key_Left:
            self.map_params.left()
        elif key == Qt.Key_Right:
            self.map_params.right()

        self.show_map()


    def show_map(self):
        map = self.uc.execute(self.map_params)

        pixmap = QPixmap()
        pixmap.loadFromData(map, 'PNG')
        self.map_label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()
