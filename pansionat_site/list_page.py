from structlog import get_logger
from pansionat_site.base import BasePage


class ListPage(BasePage):
    def __init__(self, page):
        super().__init__(page, "https://license.gov.by/license/view/")
        self.logger = get_logger()
        self.advanced_search_locator = "xpath=//div[@class='ant-collapse-header']"
        self.search_type_of_activity_box = (
            "xpath=(//div[@class='ant-select-selection__placeholder'])[4]"
        )
        self.search_type_of_activity_input_box = "xpath=//div[@class='ant-collapse-content-box']//span[text()='Вид деятельности']/following-sibling::div[1]//input"
        self.dropdown_option_locator = (
            "xpath=//li[@title='Деятельность по оказанию социальных услуг']"
        )
        self.find_button_locator = "xpath=//button[@class='ant-btn ant-btn-primary']"
        self.results_locator = (
            "xpath=//tr[@class='ant-table-row ant-table-row-level-0']//td[3]/p"
        )
        self.logger.info("list_page_initialized", url=self.url)

    def click_advanced_search(self):
        try:
            self.page.wait_for_selector(self.advanced_search_locator, state="visible")
            self.page.click(self.advanced_search_locator)
            self.logger.info("advanced_search_clicked")
        except Exception as e:
            self.logger.error("click_advanced_search_failed", error=str(e))
            raise

    def click_type_of_activity(self):
        try:
            self.page.wait_for_selector(
                self.search_type_of_activity_box, state="visible"
            )
            self.page.click(self.search_type_of_activity_box)
            self.logger.info("type_of_activity_clicked")
        except Exception as e:
            self.logger.error("click_type_of_activity_failed", error=str(e))
            raise

    def populate_type_of_activity(self, type_of_activity):
        try:
            self.page.fill(self.search_type_of_activity_input_box, type_of_activity)
            self.logger.info("type_of_activity_populated", input=type_of_activity)
        except Exception as e:
            self.logger.error("populate_type_of_activity_failed", error=str(e))
            raise

    def click_drop_down_option(self):
        try:
            self.page.click(self.dropdown_option_locator)
            self.logger.info("dropdown_option_clicked")
        except Exception as e:
            self.logger.error("click_drop_down_option_failed", error=str(e))
            raise

    def click_find_button(self):
        try:
            self.page.click(self.find_button_locator)
            self.page.wait_for_timeout(2000)
            self.logger.info("find_button_clicked")
        except Exception as e:
            self.logger.error("click_find_button_failed", error=str(e))
            raise

    def get_result_text(self):
        try:
            elements = self.page.query_selector_all(self.results_locator)
            texts = [element.text_content() for element in elements if element]
            self.logger.info("result_texts_retrieved", count=len(texts))
            return texts
        except Exception as e:
            self.logger.error("get_result_text_failed", error=str(e))
            return []
