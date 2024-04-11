class GCDComputer:
    """
    A class to compute the greatest common divisor (GCD) of two numbers
    using the Euclidean Algorithm.
    """

    def euclidean_algorithm(self, a, b):
        """
        Implementation details as previously described.
        """
        while b != 0:
            a, b = b, a % b
        return a


def main():
    # Create an instance of the GCDComputer class.
    gcd_computer = GCDComputer()

    try:
        # Request user input for the two numbers.
        a = int(input("Enter the first positive number: "))
        b = int(input("Enter the second positive number: "))

        # Check if the inputs are positive integers.
        if a <= 0 or b <= 0:
            print("Error: Both numbers must be positive integers.")
            return

        # Computing the GCD using the Euclidean Algorithm.
        print(f"The GCD of {a} and {b} is: {gcd_computer.euclidean_algorithm(a, b)}")
    except ValueError:
        # Handle the case where the input cannot be converted to an integer.
        print("Error: Please enter valid integers.")


if __name__ == "__main__":
    main()