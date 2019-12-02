import random

ppl_list = [(1940, 1956), (2007, 2011), (1957, 2011), (1933, 1960), (1974, 2011), (1955, 2011), (1950, 1999),
            (1925, 1937), (1994, 2011), (1900, 1905)]


def get_random_ppl_list(n=10):
    l = []
    for i in range(10):
        num1 = random.randrange(1900, 2010)
        num2 = min(random.randrange(num1 + 1, num1 + random.randrange(2, 110)), 2011)
        l.append((num1, num2))
    return l


def higes_pop_year(ppl_list):
    for person in ppl_list:
