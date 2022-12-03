from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="D:\\Sofware\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://meralda.scalenext.io/user/register")
driver.maximize_window()


driver.find_element(By.NAME,'first_name').send_keys('Deepak')
driver.find_element(By.NAME,'last_name').send_keys('Pal')
driver.find_element(By.NAME,'email').send_keys('deepak712452@gmail.com')
driver.find_element(By.NAME,'mobile').send_keys('9966876555')

driver.find_element(By.NAME,'date').click()
driver.find_element(By.XPATH, "(//*[@type='button'])[8]").click()

driver.find_element(By.XPATH, '(//*[@type="button"])[3]').click()
driver.find_element(By.XPATH, '(//*[@type="button"])[3]').click()
driver.find_element(By.XPATH, '(//*[@type="button"])[3]').click()

driver.find_element(By.XPATH, '//*[text()="1996"]').click()
driver.find_element(By.XPATH, '//*[text()="Nov"]').click()
driver.find_element(By.XPATH,'(//*[text()="30"])[2]').click()

driver.find_element(By.NAME,'password').send_keys('1234567890')
driver.find_element(By.NAME,'password_confirmation').send_keys('1234567890')

driver.execute_script("window.scrollBy(0, 100)")
time.sleep(3)

ele = driver.find_element(By.XPATH, " (//*[@type='submit'])[1]")
driver.execute_script("arguments[0].click();", ele)
