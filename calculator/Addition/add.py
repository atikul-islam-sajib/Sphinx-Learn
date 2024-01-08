class SimpleCalculator:
    """
    A simple calculator class to perform basic arithmetic operations.

    Methods:
    --------
    add(a, b)
        Returns the sum of two numbers a and b.
    """

    def add(self, a, b):
        """
        Add two numbers.

        Parameters:
        a (float): First number.
        b (float): Second number.

        Returns:
        float: The sum of a and b.
        """
        return a + b

# Example usage
calculator = SimpleCalculator()
result = calculator.add(10, 5)
print("The result is:", result)
