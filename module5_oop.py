class NumProcessor:
    def __init__(self):
        self.numbers = []
    def read_num(self, N):
        """The program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)"""
        for i in range(N):
            num = float(input(f"Enter number {i+1}: "))
            numbers.append(num)
    def find_numb(self, X):
        """For input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before."""
        try:
            index = self.numbers.index(X) + 1  # +1 for 1-based index
            return index
        except ValueError:
            return -1