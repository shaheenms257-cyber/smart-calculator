import math

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def sqrt(self, a):
        result = math.sqrt(a)
        self.history.append(f"sqrt({a}) = {result}")
        return result

    def power(self, a, b):
        result = math.pow(a, b)
        self.history.append(f"{a} ^ {b} = {result}")
        return result

    def sin(self, angle):
        result = math.sin(math.radians(angle))
        self.history.append(f"sin({angle}) = {result}")
        return result

    def cos(self, angle):
        result = math.cos(math.radians(angle))
        self.history.append(f"cos({angle}) = {result}")
        return result

    def tan(self, angle):
        result = math.tan(math.radians(angle))
        self.history.append(f"tan({angle}) = {result}")
        return result

    def convert_length(self, value, from_unit, to_unit):
        conversion_factors = {
            'meters': 1,
            'kilometers': 0.001,
            'miles': 0.000621371,
            'feet': 3.28084
        }
        if from_unit not in conversion_factors or to_unit not in conversion_factors:
            raise ValueError("Unsupported unit for length conversion")
        base_value = value * conversion_factors[from_unit]
        result = base_value / conversion_factors[to_unit]
        self.history.append(f"{value} {from_unit} = {result} {to_unit}")
        return result

    def convert_temperature(self, value, from_unit, to_unit):
        if from_unit == "C" and to_unit == "F":
            result = (value * 9/5) + 32
        elif from_unit == "F" and to_unit == "C":
            result = (value - 32) * 5/9
        elif from_unit == "C" and to_unit == "K":
            result = value + 273.15
        elif from_unit == "K" and to_unit == "C":
            result = value - 273.15
        else:
            raise ValueError("Unsupported unit for temperature conversion")
        self.history.append(f"{value} {from_unit} = {result} {to_unit}")
        return result

    def get_history(self):
        return self.history

# Example usage:
if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.divide(10, 2))
    print(calc.sqrt(16))
    print(calc.convert_length(1000, 'meters', 'kilometers'))
    print(calc.get_history())