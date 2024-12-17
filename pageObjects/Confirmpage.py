from selenium.webdriver.common.by import By


class Confirmpage:
    def __init__(self, driver):
        self.driver = driver

    select_country = (By.ID, "country")
    select_country_name = (By.LINK_TEXT, 'India')
    click_checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    click_purchase = (By.CSS_SELECTOR, "[type='submit']")
    check_test_success = (By.CLASS_NAME, "alert-success")

    def selecting_country(self):
        return self.driver.find_element(*Confirmpage.select_country).send_keys("ind")

    def country_by_name(self):
        self.driver.find_element(*Confirmpage.select_country_name).click()

    def clicking_checkbox(self):
        self.driver.find_element(*Confirmpage.click_checkbox).click()

    def clicking_purchase(self):
        self.driver.find_element(*Confirmpage.click_purchase).click()

    def checking_success_text(self):
        return self.driver.find_element(*Confirmpage.check_test_success).text
