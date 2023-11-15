
from datetime import datetime

from Pages.BasePage import BasePage

def after_scenario(context, scenario):
    print("end of the scenario")
    BasePage.screenShot(context)
    context.driver.quit()
