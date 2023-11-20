from lib2to3.fixes.fix_input import context

from selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver

from Config.config import TestData
from Pages.BasePage import BasePage


class HomePage(BasePage):
    """Locators That I use in Homepage"""
    All_Hamburger_Menu = (By.ID, "nav-hamburger-menu")
    Arts_And_Crafts_Menu = (By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[10]')
    Beading_And_Jewelry_Making_Menu = (By.LINK_TEXT, 'Beading & Jewelry Making')

    """Constructor of the page class"""

    def __int__(self, driver):
        super.__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Method to get the home page title"""

    def get_home_page_title(self, title):
        return self.get_title(title)
