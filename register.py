import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="D:\\Sofware\\chromedriver_win32\\chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://meralda.scalenext.io/user/register")
driver.maximize_window()

driver.find_element(By.NAME,'first_name').send_keys('Deepak')
driver.find_element(By.NAME,'last_name').send_keys('Pal')
driver.find_element(By.NAME,'email').send_keys('deepak12345@gmail.com')
driver.find_element(By.NAME,'mobile').send_keys('7777788833')

driver.find_element(By.NAME,'date').click()
driver.find_element(By.XPATH, "(//*[@type='button'])[8]").click()

exe_cond = '1996'
flag = False
while flag == False:
    table = driver.find_elements(By.XPATH,"//*[@class='mx-calendar-content']/table/tr/td")
    for i in table:
        if i.text == exe_cond:
            i.click()
            flag = True
            break 
    else:
        driver.find_element(By.XPATH, '(//*[@type="button"])[3]').click()

driver.find_element(By.XPATH, '//*[text()="Nov"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'(//*[text()="30"])[2]').click()

driver.find_element(By.NAME,'password').send_keys('1234567890')
driver.find_element(By.NAME,'password_confirmation').send_keys('1234567890')

driver.execute_script("window.scrollBy(0, 300)")
time.sleep(3)

register_ele = driver.find_element(By.XPATH, " (//*[@type='submit'])[1]")
driver.execute_script("arguments[0].click();", register_ele)
