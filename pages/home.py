
from PySide6.QtWidgets import (
    QLineEdit,
    QGroupBox,
    QFormLayout,
    QVBoxLayout,
    QLabel,
    QDateEdit,
    QTimeEdit,
    QTextEdit,
)

class Home(QGroupBox):
    def __init__(self, title=None, parent=None):
        super().__init__(title=title, parent=parent)
        self._create_layout_structure()
        self._create_itens_form()
    
    def _create_layout_structure(self):
        self._vertical_layout = QVBoxLayout()
        self.setLayout(self._vertical_layout)
        self._form_layout = QFormLayout()
        self._vertical_layout.addLayout(self._form_layout)

    def _create_itens_form(self):
        self._form_layout.addRow(QLabel("Date: "), QDateEdit())
        self._form_layout.addRow(QLabel("Time: "), QTimeEdit())
        self._form_layout.addRow(QLabel("Locations: "), QLineEdit())
        self._form_layout.addRow(QLabel("Description: "), QTextEdit())