from playwright.sync_api import Page

class BasePage:
    """
    A base class for all Page Objects. 
    It holds the Playwright Page instance.
    """
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)