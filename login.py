from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\\Sofware\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://meralda.scalenext.io/user/register")
driver.maximize_window()

login_ele = driver.find_element(By.XPATH, "//*[text()='Login']")
driver.execute_script("arguments[0].click();", login_ele)

driver.find_element(By.NAME,"username").send_keys('deepak12345@gmail.com')
driver.find_element(By.NAME,'password').send_keys('1234567890')

time.sleep(2)
driver.find_element(By.XPATH,'(//*[text()="Login"])[2]').click()
