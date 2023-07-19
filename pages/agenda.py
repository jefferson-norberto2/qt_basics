
from PySide6.QtWidgets import (
    QLineEdit,
    QGroupBox,
    QFormLayout,
    QVBoxLayout,
    QLabel,
)

class Agenda(QGroupBox):
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
        q1 = QLineEdit()
        q1.setPlaceholderText("Appoitment 1")
        q1.setEnabled(False)
        q2 = QLineEdit()
        q2.setPlaceholderText("Appoitment 2")
        q2.setEnabled(False)
        q3 = QLineEdit()
        q3.setPlaceholderText("Appoitment 3")
        q3.setEnabled(False)
        self._form_layout.addRow(QLabel("Appoitment: "), q1)
        self._form_layout.addRow(QLabel("Appoitment: "), q2)
        self._form_layout.addRow(QLabel("Appoitment: "), q3)