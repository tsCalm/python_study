from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# import chromedriver_autoinstaller

# chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("http://gs25.gsretail.com/gscvs/ko/customer-engagement/event/current-events")
# css_selector= "#gnb_menu > ul"
# try :
#   WebDriverWait(driver, 10).until(EC.presence_of_element_located(
#     By.CSS_SELECTOR, css_selector
#   ))
# except :
#   print('error')
time.sleep(2)
first_page_selector = "#contents > div.cnt > div > div > div > div > a.next2"
before_page_selector = "#contents > div.cnt > div > div > div > div > a.prev"
find_first_page_element = driver.find_element(By.CSS_SELECTOR, first_page_selector)
find_first_page_element.click()
time.sleep(2)
rows = driver.find_elements(By.TAG_NAME, "tr")
for row in rows : 
  cells = row.find_elements("tag name", "td")
  for cell in cells:
    # Get the text content of the cell
    cell_text = cell.text
    print("Cell Text:", cell_text)
    child_elements = cell.find_elements(By.XPATH, ".//*")
    for child_element in child_elements:
        child_tag_name = child_element.tag_name
        child_text = child_element.text
        child_attribute = child_element.get_attribute("attribute_name")
        if child_tag_name == "a" :
          print("이벤트 url", child_element.get_attribute('href'))
        print("Child Tag Name:", child_tag_name)
        print("Child Text:", child_text)
        print("Child Attribute:", child_attribute)
        print("--------")
# time.sleep(2)
# find_before_page_element = driver.find_element(By.CSS_SELECTOR, before_page_selector)
# find_before_page_element.click()
# print(find_before_page_element.text)
input()