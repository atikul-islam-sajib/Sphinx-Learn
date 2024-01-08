import sys
sys.path.append('./calculator')

from Addition import add
from Multiplication import mul


class SimpleCalculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    Methods:
    --------
    add(a, b)
        Returns the sum of two numbers a and b.
    """

    def mul(self, a, b):
        """
        Add two numbers.

        Parameters:
        a (float): First number.
        b (float): Second number.

        Returns:
        float: The sum of a and b.
        """
        return 100 * 200

# Example usage
calculator = SimpleCalculator()
result = calculator.mul(100, 10)
print("The result is:", result)


