from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class ArtsAndCraftsDepartmentPage(BasePage):


    Arts_Crafts_And_Sewing_Menu = (By.XPATH, '//*[@id="n/2617941011"]/span')
    Beading_And_Jewelry_Making = (By.XPATH, '//li/a[@href="/s?bbn=4954955011&rh=i%3Aspecialty-aps%2Cn%3A4954955011%2Cn%3A%212617942011%2Cn%3A12896081&ref_=nav_em__nav_desktop_sa_intl__beading_jewelry_making_0_2_8_3"]')
    Jewelry_Making_Engraving_Machines_And_Tools_Menu = (By.LINK_TEXT, "Jewelry Making Engraving Machines & Tools")
    Sort_By_Dropdown_Button = (By.CLASS_NAME, "a-dropdown-container")
    Price_High_To_Low = (By.XPATH, '//*[@id="a-popover-2"]/div/div/ul/li[3]')
    Third_Product_Of_Engraving_Machines_And_Tools = (By.XPATH, '(//div[@class="a-section a-spacing-base"])[3]')
    Review_Score = (By.XPATH, '//*[@id="acrPopover"]/span[1]/a/span')
    Price = (By.XPATH, '(//span[@class="a-price-whole"])[1]')

    """Constructor of the page class"""

    def __int__(self, driver):
        super.__init__(driver)

