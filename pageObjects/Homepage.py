from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self,driver):
        self.driver = driver
    shop = (By.CSS_SELECTOR,'a[href*="shop"]')
    check = (By.XPATH, "//a[normalize-space()='Category 2']")



    def gotoitems(self):
        return self.driver.find_element(*Homepage.shop)
    def testing(self):
        return self.driver.find_element(*Homepage.check)

