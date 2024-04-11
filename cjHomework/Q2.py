class GCDComputer:
    def euclidean_algorithm(self, a, b):
        """
        Compute the greatest common divisor (GCD) of two numbers a and b
        using the Euclidean Algorithm.

        Parameters:
        a (int): The first number.
        b (int): The second number.

        Returns:
        int: The greatest common divisor of a and b.
        """
        while b != 0:
            a, b = b, a % b
        return a

# Example usage
if __name__ == "__main__":
    gcd_computer = GCDComputer()
    a = 48
    b = 18
    print(f"The GCD of {a} and {b} is: {gcd_computer.euclidean_algorithm(a, b)}")