
# - define a UncountableError that takes in wrong_value as the only argument
# - the UncountableError should inherit ValueError
# - the UncountableError should indicate an error message like this:
#    'Invalid value for n, WRONG_VALUE. n must be greater than 0.'
#    where WRONG_VALUE should be replaced by the given value in the argument
# define your UncountableError here:




# do not change anything in the count_from_zero_to_n() function
# you may expect your UncountableError work in the following way
def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)


class UncountableError(ValueError):
    def __init__(self, wrong_value):
        super(UncountableError, self).__init__("Invalid value for n, %s. n must be greater than 0." % wrong_value)

count_from_zero_to_n(-10)