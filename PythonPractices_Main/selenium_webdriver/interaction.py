from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/tonymu/Dev/chromedriver_mac64/chromedriver"
service = Service(executable_path=chrome_driver_path)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
articlecount = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
print(articlecount.text)
# articlecount.click()

all_portals = driver.find_element(By.LINK_TEXT, 'Community portal')
#all_portals.click()

search_bar = driver.find_element(By.NAME, 'search')
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)