from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe") #Selects Chrome for webdriver

driver.get('https://www.expedia.com/')  #Selects chosen URL
driver.implicitly_wait(20)
driver.maximize_window()  #Maximizes browser window
driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a').click()  #this used href for navigation
#driver.find_element_by_name('Leavingfrom').send_keys('NYC')
def clk(path):  # Method for clicking.
    return driver.find_element_by_xpath(path).click()
def send(path, input):  # Method for sending text to imput boxes.
    return driver.find_element_by_xpath(path).send_keys(input)
clk('//*[@id="location-field-leg1-origin-menu"]/div[1]/button') # Selects Leaving from box
send('//*[@id="location-field-leg1-origin"]', 'ABQ')  # Sends ABQ to leaving from box
clk('//*[@id="location-field-leg1-origin-menu"]/div[2]/ul/li[1]/button/div/div[1]/span/strong') # Selects first option from drop down menu
clk('//*[@id="location-field-leg1-destination-menu"]/div[1]/button') # Selects Going to box

send('//*[@id="location-field-leg1-destination"]', 'NYC') # Sends NYC to Going to box
clk('//*[@id="location-field-leg1-destination-menu"]/div[2]/ul/li[1]/button/div/div[2]') #Selects first option from drop down menu
clk('//*[@id="d1-btn"]')  # Selects departing date box.
time.sleep(1)  # Allows time for calander to populate
clk('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[5]/td[6]/button') # Selects date by calendar location

clk('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[1]/div/div[2]/div/div[3]/button/span') # Clicks Done

clk('//*[@id="d2-btn"]') # Selects returning date box.

time.sleep(1)  # Allows time for calander to populate
clk('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]/button') # Selects date

clk('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/button/span') # Clicks Done

clk('//*[@id="wizard-flight-pwa-1"]/div[3]/div[2]/button')  # Clicks search button

wait=WebDriverWait(driver, 30)
time.sleep(15)  # Wait time allows page to load before moving to next step.
driver.find_element_by_xpath('//*[@id="stops-1"]').click()  # Selects the 1 stop radio.

'''
Below are two other wait to other ways to wait for and select the 1 stop box. 
el = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="stops-1"]')))
el.click()

el = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stops-1"]')))
el.click()
'''

