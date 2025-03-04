from structlog import get_logger
from pansionat_site.base import BasePage


class IndexPage(BasePage):
    def __init__(self, page):
        self.logger = get_logger()
        self.url = "https://license.gov.by/"
        self.search_box_locator = "xpath=//input[@class='ant-input ant-input-lg']"
        self.dropdown_locator = "xpath=//a[text()='Расширенный поиск']"
        super().__init__(page, self.url)
        self.logger.info("page_initialization", url=self.url, action="initialize")

    def is_logo_visible(self):
        try:
            self.page.wait_for_selector(
                self.search_box_locator, state="visible", timeout=5000
            )
            is_visible = self.page.is_visible(self.search_box_locator)
            self.logger.info(
                "check_visibility",
                locator=self.search_box_locator,
                visibility=is_visible,
            )
            return is_visible
        except Exception as e:
            self.logger.error(
                "visibility_check_failed", locator=self.search_box_locator, error=str(e)
            )
            return False

    def click_textbox(self):
        try:
            self.page.click(self.search_box_locator)
            self.logger.info(
                "click_action", action="click", locator=self.search_box_locator
            )
        except Exception as e:
            self.logger.error(
                "click_failed", locator=self.search_box_locator, error=str(e)
            )
            raise

    def click_dropdown(self):
        try:
            self.page.wait_for_selector(
                self.dropdown_locator, state="visible", timeout=5000
            )
            self.page.click(self.dropdown_locator)
            self.logger.info(
                "dropdown_click", action="click", locator=self.dropdown_locator
            )
        except Exception as e:
            self.logger.error(
                "dropdown_click_failed", locator=self.dropdown_locator, error=str(e)
            )
            raise
