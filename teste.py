import sys
from PySide6.QtWidgets import (
    QApplication,
    QLineEdit,
    QTextEdit,
    QDateEdit,
    QTimeEdit,
    QMainWindow,
    QGroupBox,
    QFormLayout,
    QVBoxLayout,
    QLabel,
)


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("QMainWindow")
        self.q_box = QGroupBox("Appointment Details")
        self.setCentralWidget(self.q_box)
        self._create_layouts()
        self._create_itens_form()

    def _create_layouts(self):
        self.vertical_layout = QVBoxLayout()
        self.q_box.setLayout(self.vertical_layout)
        self._form_layout = QFormLayout()
        self.vertical_layout.addLayout(self._form_layout)

    def _create_itens_form(self):
        self._form_layout.addRow(QLabel("Date: "), QDateEdit())
        self._form_layout.addRow(QLabel("Time: "), QTimeEdit())
        self._form_layout.addRow(QLabel("Locations: "), QLineEdit())
        self._form_layout.addRow(QLabel("Description: "), QTextEdit())


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
