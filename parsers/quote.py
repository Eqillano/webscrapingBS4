from locators.quote_locators import QuoteLocators

class QuoteParser:
    def __init__(self,parent):
        self.parent = parent


    def __str__(self):
        return "Quote {} , by {}".format(self.content,self.author)


    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [e.string for e in self.parent.select(locator).string]
