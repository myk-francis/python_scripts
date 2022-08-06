import enum
import re
import time
import logging
from pip import main
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from sqlalchemy import all_ 

logging.basicConfig(filename='reportLOGS.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p %Z')

def snitch_alarms_to_file():

    print("\n")
    

    browser = webdriver.Firefox()
    browser.get('http://truesecuritygps.net/Skins/DefaultIndex_EN/')

    userElem = browser.find_element(By.ID, 'txtUserName')
    userElem.send_keys('Truesecurity')
    passwordElem = browser.find_element(By.ID, 'txtPwd')
    passwordElem.send_keys('TrueGPS123!')
    passwordElem.submit()


    try:
        monitoring_button = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Monitoring"))
        )
        time.sleep(10)
        monitoring_button.click()
    except NoSuchElementException:
        logging.info('Monitoring Link Missing')
        return False
    finally:
        logging.info('Monitoring Link Found')
        
    try:
        browser.switch_to.window(browser.window_handles[1])
    except Exception as e:
        logging.info('Failed to switch windows \n')
        logging.info(e)
    else:
        logging.info('Switched Windows \n')


    try:
        something = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.ID, "mUrl"))
        )
        browser.switch_to.frame(browser.find_element(By.ID, 'mUrl'))
    except NoSuchElementException:
        logging.debug("Missing Frame")
        return False
    else:
        logging.debug("Found Frame\n")


    try:
        time.sleep(30)
        max_button = browser.find_element(By.XPATH, '//div[@id="newnotice"]')
        max_button.click()
    except Exception as e:
        print(e)
        logging.debug("Missing Element - Max button")
        return False
    else:
        logging.debug("Found the Max button\n")


    try:
        time.sleep(10)
        max_button = browser.find_element(By.XPATH, '//label[@id="toMaxest"]')
        max_button.click()
    except Exception as e:
        print(e)
        logging.debug("Missing Element - Max button")
        return False
    else:
        logging.debug("Found the Max button\n")

    try:
        final_alarms_list = []
        main_alarms_list = []
        alarms_list = []
        local_list = []
        missing_indicator = []
        count = 0

        while True:
            pbar = tqdm(total=100, ascii=True, desc="Checking")

            time.sleep(60)

            pbar.update(20)

            all_data = browser.find_elements(By.XPATH, '//div[@id="newnotice"]//div[@id="noticecon"]//table//tbody//td')

            pbar.update(20)

            for data in all_data:
                count += 1
                local_list.append(str(data.text))

                if len(alarms_list) < 5:
                    if count == 8:
                        count = 0
                        if bool(re.match(r'^[A-Z]', local_list[0])):
                            alarms_list.append(local_list)
                        
                        local_list = []

            pbar.update(20)


            if len(main_alarms_list) == 0:
                main_alarms_list = alarms_list
                final_alarms_list = main_alarms_list
                for main_alarm in main_alarms_list:
                    print(f'Truck: {main_alarm[0]}')
                    print(f'Alarm Type: {main_alarm[1]}')
                    print(f'Alarm Time: {main_alarm[2]}')
                    print(f'Speed: {main_alarm[4]}')
                    print(f'Description: {main_alarm[6]}')
                    print(f'Location: \n\n')

                alarms_list = []

            pbar.update(20)
                
            if (len(main_alarms_list) > 0) and (len(alarms_list) > 0):
                for alarm in alarms_list:
                    for main_alarm in main_alarms_list:
                        if alarm[0] not in main_alarm:
                            missing_indicator.append(True)
                        else:
                            missing_indicator.append(False)


                    if all(missing_indicator) == True:
                        print("\n\n\n-----------------NEW ALARM ADDED---------------\n")
                        main_alarms_list.append(alarm)
                        print(f'Truck: {alarm[0]}')
                        print(f'Alarm Type: {alarm[1]}')
                        print(f'Alarm Time: {alarm[2]}')
                        print(f'Speed: {alarm[4]}')
                        print(f'Description: {alarm[6]}')
                        print(f'Location: \n\n')

                    missing_indicator = []

                alarms_list = []

            pbar.update(20)
            pbar.close()
        

    except Exception as e:
        logging.debug("Missing Element - TABLE")
        print(e)
    else:
        logging.debug("Found - TABLE\n")
    
    print("\n")
    exit()

    #-----------------THIS IS WHERE WE BEGIN----------------------

snitch_alarms_to_file()
