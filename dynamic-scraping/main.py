import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


os.environ['PATH'] += r"C:/selenium"

driver = webdriver.Chrome()


print("--------------------------------binary calculator--------------------------------")
driver.get("https://www.calculator.net/binary-calculator.html")
driver.implicitly_wait(10)

input_box_1 = driver.find_element(By.NAME, "number1")
input_box_1.send_keys("101010")

input_box_2 = driver.find_element(By.NAME, "number2")
input_box_2.send_keys("101010")

calculate_button = driver.find_element(By.NAME, "x")
calculate_button.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CLASS_NAME, "h2result") #the element to be PRESENT
    )
)

try:
    result = driver.find_element(By.CLASS_NAME, "h2result").text
    print(result)
except:
    print("No such element found")



print("--------------------------------spotify download--------------------------------")
driver.get("https://www.spotify.com/de-en/download/other/")
driver.implicitly_wait(10)  #if the element is found within 10 seconds, it will move on to the next line



download_button = driver.find_elements(By.CSS_SELECTOR, "[data-encore-id='textLink']")
download_button[6].click()



print("--------------------------------google search--------------------------------")
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium")
search_box.submit()

search_button = driver.find_element(By.NAME, "btnK")
search_button.click()


"""
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.ID, "download-button"), #the element to be clicked
        "Download button is not clickable" #the message to be displayed if the element is not clickable
    )
)

download_button.click()

"""



