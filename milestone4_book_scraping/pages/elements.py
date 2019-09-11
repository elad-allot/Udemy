from bs4 import BeautifulSoup
from locators.entity_locators import EntityLocators
from parsers.book import BookParser
from parsers.category import CategoryParser


class PageElements:
    def __init__(self, page_content, page_url=''):
        self.soup = BeautifulSoup(page_content, 'html.parser')
        self.page_url = page_url

    @property
    def book_product(self):
        locator = EntityLocators.BOOKS
        book_products = self.soup.select(locator)
        return [BookParser(book) for book in book_products]

    @property
    def categorie_list(self):
        locator = EntityLocators.CATEGORY
        categories = self.soup.select(locator)
        # print(categories)
        return [CategoryParser(cat, self.page_url) for cat in categories]

    @property
    def next_button(self):
        pass