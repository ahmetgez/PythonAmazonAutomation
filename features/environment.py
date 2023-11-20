

def after_scenario(context, scenario):
    print("end of the scenario")
    context.driver.save_screenshot('screenshots/selenium-save-screenshot.png')
    context.driver.quit()