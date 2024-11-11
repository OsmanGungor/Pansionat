import pytest
from playwright.sync_api import sync_playwright
from pansionat_site.pagefactory import PageFactory


@pytest.fixture(scope="function")
def create_page_factory():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    _page = context.new_page()
    yield PageFactory(_page)
    _page.close()
    context.close()
    browser.close()
    playwright.stop()