import pytest
import requests
from playwright.sync_api import sync_playwright
from requests.adapters import HTTPAdapter, Retry

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


@pytest.fixture(scope="session")
def session():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[status for status in range(201, 600)],
        raise_on_status=False,
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    yield session
    session.close()
