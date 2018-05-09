
# -*- coding: utf-8 -*-
"""
@author: Gaurav Bodara
"""


#Import all these modules
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait



#Initialize the document for writing to it the user data in word format


#Add heading


#Open chrome and go to specified url 
url="http://buy.mi.com/in/buy/product/redmi-note5"
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()


def function_login():
    Username='Enter here you mi username'
    Password='Eneter password'


    #For finding the username textfield and password textfield using xpath
    emailFieldID='username'
    passFieldID='pwd'
    loginButtonpath='//*[@id="login-button"]'
    
    
    #Find elements for login purpose and sends username and password in the textfield and find login button and clicks on it
    emailFieldElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_id(emailFieldID))
    passFieldElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_id(passFieldID))
    loginButtonElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(loginButtonpath))
    emailFieldElem.clear()
    emailFieldElem.send_keys(Username)
    passFieldElem.clear()
    passFieldElem.send_keys(Password)
    loginButtonElem.click()


#color check
color_button='//*[@id="J_proStep"]/div[2]/div[1]/ul/li[1]'
color_buttonElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(color_button))
color_buttonElem.click()

buy_now = '//*[@id="J_nextBtn"]'
buy_nowElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(buy_now))
if buy_nowElem:
    buy_nowElem.click()
else:
    print("NOt")
    
sign_in='//*[@id="J_signEntries"]/ul/li[1]/a'
sign_inElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(sign_in))
sign_inElem.click()
function_login()



next_button='/html/body/div[2]/div/div[1]/a'
if WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(next_button)):
    WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(next_button)).click()

checkout='//*[@id="mi_checkout"]'
checkoutElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(checkout))
checkoutElem.click()


#username and password
#Replace these with your own valid username and password


address='/html/body/div[3]/div[2]/div/div[2]/dl'
addressElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(address))
addressElem.click()


checkout_again='//*[@id="checkoutFormBtn"]'
checkout_againElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(checkout_again))
checkout_againElem.click()

cash_on_delivery='/html/body/div[2]/div[2]/div[2]/div[1]/div[7]'
cash_on_deliveryElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(cash_on_delivery))
cash_on_deliveryElem.click()

pay_on_delivery='/html/body/div[2]/div[2]/div[2]/div[2]/div[7]/div/div[2]/a'
pay_on_deliveryElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(pay_on_delivery))
pay_on_deliveryElem.click()



'''
verification='/html/body/div[2]/div[2]/div[2]/div[2]/div[7]/div/div[2]/div[2]/a'
verificationElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(verification))
verificationElem.click()


verify_code='/html/body/div[2]/div[2]/div[2]/div[2]/div[7]/div/div[4]/a'
verify_codeElem=WebDriverWait(driver,1).until(lambda driver: driver.find_element_by_xpath(verify_code))
verify_codeElem.click()
'''






driver.quit()
