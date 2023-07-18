# f_layout.py

"""Form layout example."""

import sys

from PySide6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
)

app = QApplication([])
window = QWidget()
window.setWindowTitle("QFormLayout")

qline_name = QLineEdit()

layout = QFormLayout()
layout.addRow("Name:", qline_name)
layout.addRow("Age:", QLineEdit())
layout.addRow("Job:", QLineEdit())
layout.addRow("Hobbies:", QLineEdit())
window.setLayout(layout)

print(qline_name.text())

window.show()
sys.exit(app.exec())