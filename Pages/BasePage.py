import time
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def launch_browser(context):
        context.driver = webdriver.Chrome()


    def do_click(self, element):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.element_to_be_clickable(element)).click()



    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def screenShot(context, self):
        context.driver.save_screenshot(self, "\PycharmProjects\pythonProject\screenshots" + str(datetime.now()) + '.png')




