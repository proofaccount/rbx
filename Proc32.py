import time 
import random
import math
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from tkinter import Tk 

#Made by TekMage 10/28/2020

import random
import string


####My files

import Find_Accs as Fa



def startup():

    print('Type L to import item List otherwise hit enter')

    list_check = input()

    pnput = "L"

    if pnput in list_check:
        print('Make sure your list is under list.txt vertically')

        main_list()

    else:
        main_single()

###################################

 
def main_single():

    print("Type your item ID")

    itmid = input()

    print("Type your max Hour ago Purhcased Time")
    
    hrsnpt = input()

    chrome_options = Options()

    #Keyword searched in the chrometest

    chrome_options.add_argument('--user-data-dir=User Data')

    chrome_options.add_argument('--profile-directory=Profile 1')


    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(chrome_options=chrome_options)
 
    #print("Type your item ID")
    #itmid = input()

    partiallink = "https://www.rolimons.com/item/"

    fullink = partiallink + itmid
    
    print(fullink)


    #driver.get("https://www.rolimons.com/itemtable")

    driver.get(fullink)

    time.sleep(300)

    try:
        driver.find_element_by_xpath('//*[@href="#allcopiestable"]').click()
        print("premium")

        time.sleep(.3)

        driver.find_elements_by_xpath('//*[@aria-label="Owned Since: activate to sort column ascending"]')[2].click()

        time.sleep(.3)

        driver.find_elements_by_xpath('//*[@aria-label="Owned Since: activate to sort column ascending"]')[2].click()

        time.sleep(1)

        select = Select(driver.find_element_by_xpath('//select[@name="all_copies_table_length"]'))
        select.select_by_value('50')

        x = 10

    except:
        print("not premium")

        time.sleep(.3)
        driver.find_elements_by_xpath('//*[@aria-label="Owned Since: activate to sort column ascending"]')[0].click()

        time.sleep(.3)
        driver.find_elements_by_xpath('//*[@aria-label="Owned Since: activate to sort column ascending"]')[0].click()

        select = Select(driver.find_element_by_xpath('//select[@name="bc_owners_table_length"]'))
        select.select_by_value('50')

        x = 0
        pass


    time.sleep(3)

    print("Page loaded")

    #While loop

    print("___________")

    #print("Max Hour ago Purhcased Time")
    
    #hrsnpt = input()
    

    hrsval = int(hrsnpt)

    hrsval+=1

    print(hrsval)

    print("___________")
    emf = open("users.txt", "w")
    bwa = open("banlist.txt", "a")

    
    while x < 60:
        try:
            #print('ran')
            user = (driver.find_elements_by_xpath("//div/table/tbody/tr/td/a[contains(@href, '/player')]")[x].get_attribute("innerText"))

            #user2 = (driver.find_elements_by_xpath("//div/table/tbody/tr/td/a")[y].get_attribute("href"))


            #//div/table/tbody/tr/td/a[@class]

            strusr = str(user)

            userfinal = strusr.replace('/trade', "")

            #Hours Ago
            hourval = (driver.find_elements_by_xpath("//div/table/tbody/tr/td[contains(@class, 'sorting_1')]")[x].get_attribute("innerText"))

            tipme = str(hourval)
            
            #print(hourval)

            min = "minutes"
            n = "an"

            #print(tipme)
            time.sleep(.1)

            if min in tipme or n in tipme:
                #print("Time under or is hour")
                print(user)
          
                linkar = str(driver.find_elements_by_xpath("//*[contains(@href, '/users')][not(contains(@href,'trade'))]")[x].get_attribute('href'))
                emf.write(linkar + "\n")
                bwa.write(linkar + "\n")
                print(linkar)
                
                print(text)
                
                print("__")
                                           
                ##Write this out
            else:
                #print("standard hours ago")
                txt = int(tipme.replace("hours ago", ""))

                if txt < hrsval:
                    print(userfinal)

                    linkar = str(driver.find_elements_by_xpath("//*[contains(@href, '/users')][not(contains(@href,'trade'))]")[x].get_attribute('href'))
                    emf.write(linkar + "\n")
                    bwa.write(linkar + "\n")
                    print(linkar)

                    print(text)
                   
                    print(txt)
                    print("__")
                else:
                    #print("bricked")
                    time.sleep(.1)

                

            #driver.find_element_by_xpath()
        except:
            pass
        #print("|")
        time.sleep(.1)
        x+=1
        
    print('OVR')
    emf.close()
    time.sleep(10)


def main_list():

    itm = open("list.txt", "r")

    print("Type your max Hour ago Purhcased Time")
    
    hrsnpt = input()

    itnpt = 0

    while itnpt < 5:
        checkr = itm.readline()
        time.sleep(1)
        print(checkr)
        itnpt+=1

        print("Item ID is:")
        
        itmid = checkr

        print(itmid)



        time.sleep(2)

        
        
        chrome_options = Options()

        #Keyword searched in the chrometest

        chrome_options.add_argument('--user-data-dir=C:/Users/arcaz/Documents/GitHub/rbx_trader/User Data')

        chrome_options.add_argument('--profile-directory=Profile 1')


        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(chrome_options=chrome_options)

        #print("Type your item ID")
        #itmid = input()

        partiallink = "https://www.rolimons.com/item/"

        fullink = partiallink + itmid
        
        print(fullink)


        #driver.get("https://www.rolimons.com/itemtable")

        driver.get(fullink)

        time.sleep(3)

        try:
            driver.find_element_by_xpath('//*[@href="#allcopiestable"]').click()
            print("premium")

            time.sleep(.3)

            driver.find_elements_by_xpath('//*[@aria-label="Owned Since: activate to sort column ascending"]')[2].click()

            time.sleep(.3)

            driver.find_elements_by_xpath('//*[@aria-label="Owned Since: activate to sort column ascending"]')[2].click()

            time.sleep(1)

            select = Select(driver.find_element_by_xpath('//select[@name="all_copies_table_length"]'))
            select.select_by_value('50')

            x = 10

        except:
            print("not premium")

            time.sleep(.3)
            driver.find_elements_by_xpath('//*[@aria-label="Owned Since: activate to sort column ascending"]')[0].click()

            time.sleep(.3)
            driver.find_elements_by_xpath('//*[@aria-label="Owned Since: activate to sort column ascending"]')[0].click()

            select = Select(driver.find_element_by_xpath('//select[@name="bc_owners_table_length"]'))
            select.select_by_value('50')

            x = 0
            pass


        time.sleep(3)

        print("Page loaded")

        #While loop

        print("___________")

        #print("Max Hour ago Purhcased Time")
        
        #hrsnpt = input()
        

        hrsval = int(hrsnpt)

        hrsval+=1

        print(hrsval)

        print("___________")
        emf = open("users.txt", "w")
        bwa = open("banlist.txt", "a")

        
        while x < 60:
            try:
                #print('ran')
                user = (driver.find_elements_by_xpath("//div/table/tbody/tr/td/a[contains(@href, '/player')]")[x].get_attribute("innerText"))

                #user2 = (driver.find_elements_by_xpath("//div/table/tbody/tr/td/a")[y].get_attribute("href"))


                #//div/table/tbody/tr/td/a[@class]

                strusr = str(user)

                userfinal = strusr.replace('/trade', "")

                #Hours Ago
                hourval = (driver.find_elements_by_xpath("//div/table/tbody/tr/td[contains(@class, 'sorting_1')]")[x].get_attribute("innerText"))

                tipme = str(hourval)
                
                #print(hourval)

                min = "minutes"
                n = "an"

                #print(tipme)
                time.sleep(.1)

                if min in tipme or n in tipme:
                    #print("Time under or is hour")
                    print(user)
            
                    linkar = str(driver.find_elements_by_xpath("//*[contains(@href, '/users')][not(contains(@href,'trade'))]")[x].get_attribute('href'))
                    emf.write(linkar + "\n")
                    bwa.write(linkar + "\n")
                    print(linkar)
                    
                    print(text)
                    
                    print("__")
                                            
                    ##Write this out
                else:
                    #print("standard hours ago")
                    txt = int(tipme.replace("hours ago", ""))

                    if txt < hrsval:
                        print(userfinal)

                        linkar = str(driver.find_elements_by_xpath("//*[contains(@href, '/users')][not(contains(@href,'trade'))]")[x].get_attribute('href'))
                        emf.write(linkar + "\n")
                        bwa.write(linkar + "\n")
                        print(linkar)

                        print(text)
                    
                        print(txt)
                        print("__")
                    else:
                        #print("bricked")
                        time.sleep(.1)

                    

                #driver.find_element_by_xpath()
            except:
                pass
            #print("|")
            time.sleep(.1)
            x+=1
        
            
        print('OVR')
        driver.close()
        time.sleep(3)
        emf.close()
        Fa.execute()
        time.sleep(1)





startup()



