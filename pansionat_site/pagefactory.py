from pansionat_site.index_page import IndexPage
from pansionat_site.list_page import ListPage


class PageFactory:
    def __init__(self, page):
        self.page = page

    def get_page_instance(self, page_name):
        if page_name == 'index_page':
            return IndexPage(self.page)
        elif page_name == 'list_page':
            return ListPage(self.page)
        else:
            raise f"Unable to create the instance of: {page_name})"



