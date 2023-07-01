from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

url = "http://gs25.gsretail.com/gscvs/ko/customer-engagement/event/current-events"

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--headless=new")
options.add_experimental_option("detach", True)

"""
paginNums = 크롤링한 페이징 넘버
currentPage = 현재 페이지
currentList = 현재 페이지의 아이템목록

"""

driver = webdriver.Chrome(options=options)
driver.get(url)

time.sleep(2)

temp = driver.find_element(By.CLASS_NAME, "num")
for one in temp :
  print(one)
  
print(temp)

driver.quit()