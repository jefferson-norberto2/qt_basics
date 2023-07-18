from PySide6.QtWidgets import QApplication
from py_calc_window import PyCalcWindow
from py_calc_controller import PyCalcController
from py_calc_model import PyCalcModel
import sys

def main():
    """PyCalc's main function."""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    PyCalcController(model=PyCalcModel.evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())

if __name__ == "__main__":
    main()