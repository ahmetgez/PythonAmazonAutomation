
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def do_click(self, element):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(element)).click()

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def screenShot(self):
        self.driver.save_screenshot('/PycharmProjects/pythonProject/screenshots/' + str(datetime.now()) + '/.png')
