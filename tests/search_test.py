import pytest
from pansionat_site.index_page import IndexPage
from pansionat_site.list_page import ListPage
from utils.common_utilities import compare_and_update_file

@pytest.mark.parametrize('search_term',['Деятельность по оказанию социальных услуг'])
def test_visit_license_website(create_page_factory, search_term):
    page_factory=create_page_factory
    index_page = page_factory.get_page_instance('index_page')
    index_page.go_to()
    index_page.click_textbox()
    index_page.click_dropdown()
    assert index_page.is_logo_visible()
    list_page = page_factory.get_page_instance('list_page')
    list_page.click_advanced_search()
    list_page.click_type_of_activity()
    list_page.populate_type_of_activity(search_term)
    list_page.click_drop_down_option()
    list_page.click_find_button()
    result_list=list_page.get_result_text()
    compare_and_update_file("C:\\Users\\osman_gungor\\Desktop\\pansionat\\List.txt", result_list)

