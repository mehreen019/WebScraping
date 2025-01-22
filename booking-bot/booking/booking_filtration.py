#This file will include a class with instance methods.
#That will be responsible to interact with our website
#After we have some results, to apply filtrations.
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[data-filters-group="class"]')
        ))
        
        for star_value in star_values:
            star_child_elements = self.wait.until(EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '[data-filters-item="class:class"]')
            ))
            
            for star_element in star_child_elements:
                try:
                    if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                        star_element.click()
                except:
                    continue

    def sort_price_lowest_first(self):
        filter_element = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="sorters-dropdown"]')
        filter_element.click()
        price_element = self.driver.find_element(By.CSS_SELECTOR, 'li[data-id="price"]')
        price_element.click()