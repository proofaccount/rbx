import time 
import random
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

import random
import string








def execute():

    chrome_options = Options()

    #Keyword searched in the chrometest

    chrome_options.add_argument('--user-data-dir=User Data')

    chrome_options.add_argument('--profile-directory=Profile 1')


    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)


    time.sleep(1)

    mnt = 0
    try:
        while 1:
            #print("Init")
            emf = open("users.txt", "r")

            x = emf.readlines()[mnt]

            #print(x)

            driver.get(x)

            time.sleep(1.5)

            
            try:
                #Message Click
                driver.find_elements_by_xpath('//div/ul/li/button[@class="btn-control-md ng-binding"]')[0].click()
                #Message Click

                time.sleep(.5)

                #Subject contents
                driver.find_elements_by_xpath('//input[@type="text"]')[1].send_keys("nope")
                #Subject contents

                time.sleep(.5)

                msgcnt = open("msg.txt", "r")

                val = msgcnt.readlines()

                #Paragraph contents
                driver.find_element_by_xpath('//*[@class="messages-reply-box border text-box text new-message-body"]').send_keys(val)
                #Paragraph contents

                time.sleep(3)

                #send btn
                driver.find_element_by_xpath('//a[@class="btn-primary-md btn-min-width send-btn"]').click()
                #send btn

                print("message cooldown 10 seconds")
                mnt+=1
                time.sleep(30)

            except:
                print("Contact settings incompatible")
                mnt+=1
                pass
            
            time.sleep(.5)

            time.sleep(3)
    except:
        pass

    print("Messages Sent")

    time.sleep(100)




