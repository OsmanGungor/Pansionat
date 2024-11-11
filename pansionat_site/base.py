from playwright.sync_api import Page
from utils.logging_config import get_logger

class BasePage:
    def __init__(self, page, url):
        self.page = page
        self.url = url
        self.logger = get_logger()
        self.logger.info("page_initialized", url=self.url)

    def go_to(self):
        try:
            self.page.goto(self.url)
            self.logger.info("navigate_to_url", action="page navigation", url=self.url)
        except Exception as e:
            self.logger.error("navigation_error", url=self.url, error=str(e))
            raise

    def is_at_url(self):
        at_url = self.page.url == self.url
        self.logger.info("current_url_check", expected_url=self.url, current_url=self.page.url, is_at_url=at_url)
        return at_url