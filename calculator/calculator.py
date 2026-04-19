import math
import re

class Calculator:
    def __init__(self):
        self.history = []

        self.allowed_functions = {
            "sqrt": math.sqrt,
            "pow": pow,
            "log": math.log,
            "log10": math.log10,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "abs": abs,
            "fact": math.factorial
        }

        self.allowed_constants = {
            "pi": math.pi,
            "e": math.e
        }

    def is_safe_expression(self, expr):
        return re.match(r'^[0-9+\-*/().,^ a-zA-Z]*$', expr)

    def evaluate(self, expression):
        try:
            # Convert ^ to **
            expression = expression.replace("^", "**")

            if not self.is_safe_expression(expression):
                return "Invalid Input"

            safe_dict = {}
            safe_dict.update(self.allowed_functions)
            safe_dict.update(self.allowed_constants)

            result = eval(expression, {"__builtins__": None}, safe_dict)

            self._add_to_history(expression, result)

            return result

        except Exception:
            return "Invalid Expression"

    def _add_to_history(self, expression, result):
        entry = f"{expression} = {result}"
        self.history.append(entry)

        if len(self.history) > 10:
            self.history.pop(0)

    def get_history(self):
        return self.history