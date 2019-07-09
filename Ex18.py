# Define a PrimeGenerator class
class PrimeGenerator:
    # You may modify the __init__() method if necessary, but you don't need to change its arguments
    def __init__(self, stop):
        self.stop = stop    # stop defines the range (exclusive upper bound) in which we search for the primes
        self.current = 2

    def __next__(self):
        for n in range(self.current, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                self.current = n+1
                return n
        raise StopIteration()

# g = PrimeGenerator(20)
#
# while True:
#     print(next(g))
#
