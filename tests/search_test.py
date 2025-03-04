import pytest
from utils.common_utilities import (
    compare_and_write_file,
    send_windows_notification,
    send_email_notification,
)


@pytest.mark.parametrize("search_term", ["Деятельность по оказанию социальных услуг"])
def test_visit_license_website(create_page_factory, search_term):
    page_factory = create_page_factory
    index_page = page_factory.get_page_instance("index_page")
    index_page.go_to()
    index_page.click_textbox()
    index_page.click_dropdown()
    assert index_page.is_logo_visible()
    list_page = page_factory.get_page_instance("list_page")
    list_page.click_advanced_search()
    list_page.click_type_of_activity()
    list_page.populate_type_of_activity(search_term)
    list_page.click_drop_down_option()
    list_page.click_find_button()
    result_list = list_page.get_result_text()
    is_updated = compare_and_write_file("List.txt", result_list)
    send_windows_notification(is_updated)
    send_email_notification(is_updated)
