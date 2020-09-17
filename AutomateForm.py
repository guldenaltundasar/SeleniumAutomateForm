from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path="/Users/galtu/Downloads/selenium/chromedriver")
driver.get("https://rahulshettyacademy.com/angularpractice/")

name = driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("Gülden Altundaşar")
mail = driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[2]/input").send_keys("test@gmail.com")
password = driver.find_element_by_xpath("//*[@id='exampleInputPassword1']").send_keys("Password")
check_box = driver.find_element_by_xpath("//*[@id='exampleCheck1']").click()
dropdown = Select(driver.find_element_by_xpath("//*[@id='exampleFormControlSelect1']")).select_by_visible_text("Female")
radio = driver.find_element_by_xpath("//*[@id='inlineRadio2']").click()
date = driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/div[7]/input").send_keys("18.01.1996")
button = driver.find_element_by_xpath("/html/body/app-root/form-comp/div/form/input").click()
message = driver.find_element_by_xpath("/html/body/app-root/form-comp/div/div[2]/div").text

assert "success" in message

time.sleep(2)
driver.close()



