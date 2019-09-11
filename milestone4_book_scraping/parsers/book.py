import re
from locators.entity_properties import BookProduct


class BookParser:
    rating_parser = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    def __init__(self, parent):
        self.parent = parent


    def __repr__(self):
        return f'<Book: {self.title}, Price: {self.price}, Rating: {self.rating}/5 \n'

    @property
    def title(self):
        locator = BookProduct.TITLE
        return self.parent.select_one(locator).attrs['title']

    @property
    def price(self):
        locator = BookProduct.PRICE
        item_price = self.parent.select_one(locator).string
        # item_price = soup.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        reg = re.search(pattern, item_price)
        return float(reg.group(1))

    @property
    def rating(self):
        locator = BookProduct.RATING
        # self.parent.select_one(locator).attrs['title']
        classes = self.parent.select_one(locator).attrs['class']
        return self.rating_parser.get(next(filter(lambda x: x != 'star-rating', classes)).lower(), 0)

