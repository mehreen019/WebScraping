import booking.constants as const
import os
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)
        print("Landing first page")
        self.dismiss_signin_popup()

    def dismiss_signin_popup(self):
        
        print("Dismissing sign in popup")

        try:
            close_button = self.find_element(By.CSS_SELECTOR,
                '[aria-label="Dismiss sign in info."]')
            close_button.click()
        except Exception as e:
            print('could not find the close button')
            print(e)

    def change_currency(self, currency="BDT"):
        currency_element = self.find_element(By.CSS_SELECTOR,
            '[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        # Wait for currency options and select BDT by text content
        currency_selection = self.find_element(By.XPATH,
            f"//span[contains(@class, 'Picker_selection-text') and contains(text(), '{currency}')]"
        )
        currency_selection.click()


    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, 'ss')
        search_field.clear()
        search_field.send_keys(place_to_go)

        time.sleep(3);

        first_result = self.find_element(By.ID,
            'autocomplete-result-0'
        )
        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(By.CSS_SELECTOR,
            f'[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(By.CSS_SELECTOR,
            f'[data-date="{check_out_date}"]'
        )
        check_out_element.click()

    def select_adults(self, count=1):
        selection_element = self.find_element(By.ID, 'xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element(By.CSS_SELECTOR,
                '[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            #If the value of adults reaches 1, then we should get out
            #of the while loop
            adults_value_element = self.find_element(By.ID, 'group_adults')
            adults_value = adults_value_element.get_attribute(
                'value'
            ) # Should give back the adults count

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element(By.CSS_SELECTOR,
            '[aria-label="Increase number of Adults"]'
        )

        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR,
            '[type="submit"]'
        )
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)

        filtration.sort_price_lowest_first()

    def report_results(self):
        hotel_boxes = self.find_element(By.ID,
            'hotellist_inner'
        )

        report = BookingReport(hotel_boxes)
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)