import enum
import re
import time
import logging
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from sqlalchemy import all_ 

logging.basicConfig(filename='reportLOGS.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S %p %Z')

def snitch_alarms_to_file():

    output_file = open('alarms_output.log', 'a')

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
        main_alarms_list = []
        alarms_list = []
        local_list = []
        missing_indicator = True
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
                for main_alarm in main_alarms_list:
                    output_file.write(f'Truck: {main_alarm[0]}\n')
                    output_file.write(f'Alarm Type: {main_alarm[1]}\n')
                    output_file.write(f'Alarm Time: {main_alarm[2]}\n')
                    output_file.write(f'Speed: {main_alarm[4]}\n')
                    output_file.write(f'Description: {main_alarm[6]}\n')
                    output_file.write(f'Location: \n\n')

                alarms_list = []

            pbar.update(20)
                
            if (len(main_alarms_list) > 0) and (len(alarms_list) > 0):
                for alarm in alarms_list:
                    for main_alarm in main_alarms_list:
                        if alarm[0] not in main_alarm:
                            missing_indicator = True
                        else:
                            missing_indicator = False


                    if missing_indicator == True:
                        output_file.write(f'Truck: {main_alarm[0]}\n')
                        output_file.write(f'Alarm Type: {main_alarm[1]}\n')
                        output_file.write(f'Alarm Time: {main_alarm[2]}\n')
                        output_file.write(f'Speed: {main_alarm[4]}\n')
                        output_file.write(f'Description: {main_alarm[6]}\n')
                        output_file.write(f'Location: \n\n')

                    missing_indicator = False

                
                print("\n\n\n-----------------NEW ALARM ADDED---------------\n\n\n")
                            
                alarms_list = []

            pbar.update(20)
            pbar.close()
        

    except Exception as e:
        logging.debug("Missing Element - TABLE")
        print(e)
    else:
        logging.debug("Found - TABLE\n")
    
    output_file.close()
    print("\n")
    exit()

    #-----------------THIS IS WHERE WE BEGIN----------------------

snitch_alarms_to_file()
