from locators.locators import QuoteLocators, TagLocators

class QuoteParser:
    """
    dont know yet :)
    """
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator)

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return [tag.string for tag in self.parent.select(locator)]


class TagsParser:
    curr_rank = 0

    def __init__(self, parent):
        self.parent = parent
        type(self).curr_rank += 1
        self.my_rank = self.curr_rank

    def __repr__(self):
        return f"<Tag {self.tag}, ranked {self.my_rank} >"

    @property
    def tag(self):
        locator = TagLocators.TAG
        return self.parent.select_one(locator).string

    @property
    def rank(self):
        # locator = TagLocators.RANK
        # return self.parent.select_one(locator).attrs['style']
        return self.my_rank
