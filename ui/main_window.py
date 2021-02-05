from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QLineEdit, QHBoxLayout, QPushButton

from application_service.get_map_uc import GetMapUseCase
from domain.map_params import MapParams


class MainWindow(QWidget):
    def __init__(self, uc: GetMapUseCase, parent=None):
        super().__init__(parent)

        self.map_label = QLabel(self)
        self.search_line = QLineEdit(self)
        self.search_line.setFocusPolicy(Qt.ClickFocus)
        self.search_button = QPushButton(self, text='Искать')
        self.search_button.setFocusPolicy(Qt.NoFocus)

        self.search_button.clicked.connect(self.send_search_line)

        main_layout = QHBoxLayout()
        map_layout = QVBoxLayout()
        settings_layout = QVBoxLayout()
        map_layout.addWidget(self.map_label)
        settings_layout.addWidget(self.search_line)
        settings_layout.addWidget(self.search_button)
        main_layout.addLayout(settings_layout)
        main_layout.addLayout(map_layout)

        self.setLayout(main_layout)

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
        elif key == Qt.Key_M:
            self.map_params.change_l()

        self.show_map()

    def show_map(self):
        map = self.uc.execute(self.map_params)

        pixmap = QPixmap()
        pixmap.loadFromData(map, self.map_params.get_format())
        self.map_label.setPixmap(pixmap)

    def send_search_line(self):
        # чтобы сбросить выделение с ввода текста надо нажать поиск
        response = self.uc.search_pos(self.search_line.text())
        self.map_params.set_pos(response)
        self.map_params.add_point(response)
        self.search_line.clearFocus()
        self.show_map()


if __name__ == '__main__':
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec()
