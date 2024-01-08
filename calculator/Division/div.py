import sys
sys.path.append('./calculator')

from Addition import add


class SimpleCalculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    Methods:
    --------
    add(a, b)
        Returns the sum of two numbers a and b.
    """

    def div(self, a, b):
        """
        Add two numbers.

        Parameters:
        a (float): First number.
        b (float): Second number.

        Returns:
        float: The sum of a and b.
        """
        return a / b

# Example usage
calculator = SimpleCalculator()
result = calculator.div(100, 10)
print("The result is:", result)


