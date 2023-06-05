from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users/tonymu/Dev/chromedriver_mac64/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# message = driver.find_element(By.ID,'taxInclusiveMessage')
# price = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
# print(price[0].text)

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, 'q')
print(search_bar.tag_name)
print(search_bar.get_attribute("placeholder"))

log = driver.find_element(By.CLASS_NAME, 'python-logo')
print(log.size)

documentation_link = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
print(documentation_link.text)

# using XPath, find xpath by right click on the element and copy xpath , ref https://www.w3schools.com/xml/xpath_intro.asp
submit_bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(submit_bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)

