import datetime
import time

from _pytest.outcomes import fail
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.ArtsAndCraftsDepartmentPage import ArtsAndCraftsDepartmentPage
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


@step('user navigates to Amazon website in "{driver}"')
def step_impl(context, driver):
    if driver == "chrome":
        context.driver = webdriver.Chrome()
    elif driver == "headless":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://www.amazon.com/ref=nav_logo")
    context.driver.maximize_window()
    context.driver.find_elements(By.XPATH, "//ul[@class='hmenu hmenu-visible hmenu-translateX']/li")
    time.sleep(10)  # for manually entering captcha


@then('Amazon web page is displayed')
def step_impl(context):
    title = context.driver.title
    print(title)
    assert title.__contains__(TestData.HOME_PAGE_TITLE)
    # context.driver.save_screenshot('screenshots/selenium-save-screenshot.png')


@when('user clicks on All_Hamburger_Menu')
def step_impl(self):
    BasePage.do_click(self, HomePage.All_Hamburger_Menu)


@when(u'user clicks on Arts_And_Crafts_Menu')
def step_impl(self):
    BasePage.do_click(self, HomePage.Arts_And_Crafts_Menu)


@when(u'user clicks on Beading_And_Jewelry_Making_Menu')
def step_impl(self):
    BasePage.do_click(self, HomePage.Beading_And_Jewelry_Making_Menu)


@when(u'user clicks on Arts_Crafts_And_Sewing_Menu')
def step_impl(self):
    BasePage.do_click(self, ArtsAndCraftsDepartmentPage.Arts_Crafts_And_Sewing_Menu)


@when(u'user clicks on Beading_And_Jewelry_Making')
def step_impl(self):
    BasePage.do_click(self, ArtsAndCraftsDepartmentPage.Beading_And_Jewelry_Making)


@when(u'user clicks on Jewelry_Making_Engraving_Machines_And_Tools')
def step_impl(self):
    BasePage.do_click(self, ArtsAndCraftsDepartmentPage.Jewelry_Making_Engraving_Machines_And_Tools_Menu)


@when(u'user clicks on Sort_By_Dropdown_Button')
def step_impl(self):
    BasePage.do_click(self, ArtsAndCraftsDepartmentPage.Sort_By_Dropdown_Button)


@when(u'user cliks on Price_High_To_Low')
def step_impl(self):
    BasePage.do_click(self, ArtsAndCraftsDepartmentPage.Price_High_To_Low)


@when(u'user clicks on Third_Product_Of_Engraving_Machines_And_Tools')
def step_impl(self):
    BasePage.do_click(self, ArtsAndCraftsDepartmentPage.Third_Product_Of_Engraving_Machines_And_Tools)


@then(u'user checks the review score for the selected product')
def step_impl(self):
    Review_Score = int(ArtsAndCraftsDepartmentPage.Review_Score.text())
    if Review_Score > 4:
        pass
    else:
        fail("Product's review score should be higher then 4")


@then(u'user checks the price for the selected product')
def step_impl(context):
    Product_price = int(ArtsAndCraftsDepartmentPage.Price.text())
    if Product_price > 4000:
        fail("Product Price should be less then $4000")
    else:
        pass
