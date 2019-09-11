from urllib.parse import urljoin
from locators.entity_properties import Catagories


class CategoryParser:
    def __init__(self, parent, base_url=''):
        self.parent = parent
        self.base_url = base_url

    def __repr__(self):
        return f'Category name: {self.category_name}, Link: {self.cat_link}'

    @property
    def category_name(self):
        locator = Catagories.CATEGORY_NAME
        return self.parent.select_one(locator).string.strip()

    @property
    def cat_link(self):
        locator = Catagories.CATEGORY_HREF
        return urljoin(self.base_url, self.parent.select_one(locator).attrs['href'])
