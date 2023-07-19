import sys
from pages.agenda import Agenda
from pages.perfil import Perfil
from pages.home import Home
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtCore import Qt, QFile, QTextStream
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QDockWidget,
    QPushButton,
    QStackedWidget,
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.resize(900, 600)
        self._create_layouts()
        self._create_menu()
        self._create_dock_menu()
        self._load_stylesheet()

    def _create_layouts(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self._v_box = QVBoxLayout(central_widget)
        self.stacked_widget = QStackedWidget()
        self._v_box.addWidget(self.stacked_widget)

        self._page_home = Home("Home")
        self._page_agenda = Agenda("Agenda")
        self._page_perfil = Perfil("Perfil")
        
        self.stacked_widget.addWidget(self._page_home)
        self.stacked_widget.addWidget(self._page_agenda)
        self.stacked_widget.addWidget(self._page_perfil)
        

    def _create_menu(self):
        self.w_menu = QWidget()
        self.v_menu = QVBoxLayout(self.w_menu)
        self.v_menu.setSpacing(8)
        self.v_menu.setContentsMargins(0, 0, 0, 0)

        self.b1 = QPushButton("Home")
        self.b2 = QPushButton("Agenda")
        self.b3 = QPushButton("Perfil")

        self.b1.setIcon(QPixmap("icons\\home.png"))

        self.b1.setObjectName("Button1")
        self.b2.setObjectName("Button2")
        self.b3.setObjectName("Button3")

        self.v_menu.addWidget(QLabel("Menu"))
        self.v_menu.addWidget(self.b1)
        self.v_menu.addWidget(self.b2)
        self.v_menu.addWidget(self.b3)
        self.v_menu.addStretch()

        self.b1.setCheckable(True)  # Tornar o botão "clicável"
        self.b1.setChecked(True)  # Definir o botão como pressionado
        self.b1.setEnabled(False)  # Desabilitar o botão

        self.b2.setCheckable(True)
        self.b2.setChecked(False)
        self.b2.setEnabled(True)

        self.b3.setCheckable(True)
        self.b3.setChecked(False)
        self.b3.setEnabled(True)

        self.b1.clicked.connect(lambda: self.show_page(0))
        self.b2.clicked.connect(lambda: self.show_page(1))
        self.b3.clicked.connect(lambda: self.show_page(2))

    def _create_dock_menu(self):
        self.dock_menu = QDockWidget("Menu", self)
        self.dock_menu.setAllowedAreas(Qt.LeftDockWidgetArea)

        self.dock_menu.setWidget(self.w_menu)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_menu)

        # Impede o movimento e fechamento do QDockWidget
        self.dock_menu.setFeatures(QDockWidget.NoDockWidgetFeatures)

        # Desabilita os botões de "fechar" e "flutuar"
        self.dock_menu.setTitleBarWidget(QWidget())

    def _load_stylesheet(self):
        file = QFile("styles\\qpush_button.css")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
            file.close()

    def show_page(self, index):
        self.stacked_widget.setCurrentIndex(index)
        if index == 0:
            self.b1.setEnabled(False)
            self.b1.setChecked(True)
            self.b2.setEnabled(True)
            self.b2.setChecked(False)
            self.b3.setEnabled(True)
            self.b3.setChecked(False)
        elif index == 1:
            self.b1.setEnabled(True)
            self.b1.setChecked(False)
            self.b2.setEnabled(False)
            self.b2.setChecked(True)
            self.b3.setEnabled(True)
            self.b3.setChecked(False)
        elif index == 2:
            self.b1.setEnabled(True)
            self.b1.setChecked(False)
            self.b2.setEnabled(True)
            self.b2.setChecked(False)
            self.b3.setEnabled(False)
            self.b3.setChecked(True)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
