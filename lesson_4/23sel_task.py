from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver1 = webdriver.Chrome()
driver1.get("file:///Users/danse/Downloads/tip_calc/index.html")
billamt = driver1.find_element("id", "billamt")
billamt.send_keys("100")
driver1.find_element("xpath", "//*[@id=\"serviceQual\"]/option[3]").click()
driver1.find_element("id", "peopleamt").send_keys("5")
driver1.find_element("xpath", "//*[@id=\"musicQuality\"]/option[5]").click()
driver1.find_element("id", "calculate").click()
expected = 8
actual = driver1.find_element("id", "tip").text
print("actual is: " + actual)
assert expected == actual
sleep(10)