# This file is going to include method that will parse
# The specific data that we need from each one of the deal boxes.
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()
    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements_by_class_name(
            'sr_property_block'
        )

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element(By.CSS_SELECTOR,
                '[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element(By.CSS_SELECTOR,
                '[data-testid="price-and-discounted-price"]'
            ).get_attribute('innerHTML').strip()
            hotel_score = deal_box.find_element(By.CSS_SELECTOR,
                '[data-testid="review-score"]'
            ).get_attribute('innerHTML').strip()

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection