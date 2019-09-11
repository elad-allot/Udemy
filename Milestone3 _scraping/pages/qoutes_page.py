from bs4 import BeautifulSoup

from locators.page_locators import PageLocators
from parsers.quote import QuoteParser, TagsParser

class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = PageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(qt) for qt in quote_tags]

    @property
    def tags(self):
        locator = PageLocators.TAG
        tags = self.soup.select(locator)
        # print(tags)
        return [TagsParser(t) for t in tags]
