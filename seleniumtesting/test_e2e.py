from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.Checkoutpage import Checkoutpage
from pageObjects.Confirmpage import Confirmpage
from pageObjects.Homepage import Homepage
from utilities.BaseClass import BaseClass
from datetime import datetime

class TestOne(BaseClass):


    def test_e2ew(self):

        homepage = Homepage(self.driver)
        checkoutpage = Checkoutpage(self.driver)
        confirmpage = Confirmpage(self.driver)
        homepage.gotoitems().click()
        # products = self.driver.find_elements(By.XPATH,'//div[@class="card h-100"]')
        products = checkoutpage.enterCheck()
        print(datetime.now())

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                checkoutpage.adding_to_cart(product)

        checkoutpage.clicking_checkout()
        checkoutpage.confirming_checkout()
        confirmpage.selecting_country()
        self.verifyLinkPresence("India")
        confirmpage.country_by_name()
        confirmpage.clicking_checkbox()
        confirmpage.clicking_purchase()
        successText = confirmpage.checking_success_text()
        assert "Success! Thank you!" in successText


