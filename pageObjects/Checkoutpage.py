from selenium.webdriver.common.by import By


class Checkoutpage :
    def __init__(self, driver):
        self.driver = driver
    products_list = [By.XPATH, '//div[@class="card h-100"]']
    add_to_cart = (By.XPATH, "div/button")
    click_checkout = (By.CSS_SELECTOR, 'a[class*="btn-primary"]')
    confirm_checkout = (By.XPATH, "//button[@class='btn btn-success']")
    ex = (By.XPATH, "div/h4/a")

    def enterCheck(self):
        return self.driver.find_elements(*Checkoutpage.products_list)

    def ex9(self):
         return self.driver.find_element(*Checkoutpage.ex)

    def adding_to_cart(self, product):
        product.find_element(*Checkoutpage.add_to_cart).click()

    def clicking_checkout(self):
        self.driver.find_element(*Checkoutpage.click_checkout).click()

    def confirming_checkout(self):
        self.driver.find_element(*Checkoutpage.confirm_checkout).click()
