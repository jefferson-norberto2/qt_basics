from constants import ERROR_MSG

class PyCalcModel(object):
    """PyCalc's Model."""

    @staticmethod
    def evaluateExpression(expression):
        """Evaluate an expression (Model)."""
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = ERROR_MSG
        return result