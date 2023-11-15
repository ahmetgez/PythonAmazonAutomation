import pytest

from Config.config import TestData
from Pages.HomePage import HomePage


class Test_HomePage:

    def test_home_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE



