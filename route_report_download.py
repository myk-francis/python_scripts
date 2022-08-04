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

def download_report(arg_date, arg_time):

    print("\n")
    pbar = tqdm(total=100, ascii=True, desc="Downloading")

    browser = webdriver.Firefox()
    browser.get('http://truesecuritygps.net/Skins/DefaultIndex_EN/')

    userElem = browser.find_element(By.ID, 'txtUserName')
    userElem.send_keys('Truesecurity')
    passwordElem = browser.find_element(By.ID, 'txtPwd')
    passwordElem.send_keys('TrueGPS123!')
    passwordElem.submit()

    pbar.update(10)

    try:
        monitoring_button = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Monitoring"))
        )
        time.sleep(10)
        monitoring_button.click()
    except NoSuchElementException:
        logging.debug('Monitoring Link Missing')
        return False
    finally:
        logging.debug('Monitoring Link Found')
        
    pbar.update(10)

    try:
        browser.switch_to.window(browser.window_handles[1])
    except Exception as e:
        logging.debug('Failed to switch windows \n')
        logging.debug(e)
    else:
        logging.debug('Switched Windows \n')


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

    pbar.update(10)

    try:
        time.sleep(60)
        report_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "goto_report"))
        )
        report_link = browser.find_element(By.ID, "goto_report")
        report_link.click()
    except NoSuchElementException:
        logging.debug("Missing Element - Route Link")
        return False
    else:
        logging.debug("Found Route Link\n")

    try:
        something = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.ID, "pageShowFrame"))
        )
        browser.switch_to.frame(browser.find_element(By.ID, 'pageShowFrame'))
    except NoSuchElementException:
        logging.debug("Missing Frame 2")
        return False
    else:
        logging.debug("Found Frame 2\n")

    pbar.update(10)

    try:
        time.sleep(10)
        rr_button = browser.find_element(By.LINK_TEXT,"Route report") 
        rr_button.click()
    except NoSuchElementException:
        logging.debug('Missing Element - Route Link 2')
        return False
    else:
        logging.debug('Found Route Report Link\n')

    pbar.update(10)

    try:
        something = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.ID, "custIframeTree"))
        )
        browser.switch_to.frame(browser.find_element(By.ID, 'custIframeTree'))
    except NoSuchElementException:
        logging.debug("Missing Frame 3")
        return False
    else:
        logging.debug("Found Frame 3\n")


    try:
        plus_button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "tree_4_switch"))
        )
        time.sleep(5)
        plus_button = browser.find_element(By.ID, 'tree_4_switch')
        plus_button.click()
    except NoSuchElementException:
        logging.debug("Missing Element - Plus Link Impala Terminals")
        return False
    else:
        logging.debug("Found Impala Terminals Link\n")

    pbar.update(10)

    try:
        impala_button = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "tree_9_span"))
        )
        time.sleep(5)
        impala_button = browser.find_element(By.ID, 'tree_9_span')
        impala_button.click()
    except NoSuchElementException:
        logging.debug("Missing Element - Plus Link Impala Trucks")
        return False
    else:
        logging.debug("Found Impala Trucks Link\n")


    try:
        time.sleep(5)
        browser.switch_to.parent_frame()
        time.sleep(5)
        browser.switch_to.frame(browser.find_element(By.ID, 'content-iframe'))
    except NoSuchElementException:
        logging.debug("Missing Frame 4")
        return False
    else:
        logging.debug("Found Frame 4\n")

    pbar.update(10)

    try:
        time.sleep(10)
        bg_date = browser.find_element(By.ID, 'beginTime')
        bg_date.click()

        browser.switch_to.default_content()
        logging.debug("Default Content")
        time.sleep(5)

        browser.switch_to.frame(browser.find_element(By.XPATH, '//div[@id="_my97DP"]//iframe[@src="http://truesecuritygps.net/My97DatePicker/My97DatePicker.htm"]'))
        logging.debug("Found Frame")

        time.sleep(2)
        all_dates = browser.find_elements(By.XPATH, '//div[@class="WdateDiv"]//table[@class="WdayTable"]//tbody//tr//td[@class="Wwday" or @class="Wday" or @class="WotherDay"]')

        for date_element in all_dates:
            date = date_element.text
            logging.debug(date)
            if date == str(int(arg_date) - 1):
                date_element.click()
                break

        time.sleep(2)
        browser.find_element(By.XPATH, '//div[@class="WdateDiv"]//div[@id="dpTime"]//table[@cellspacing="0"][@cellpadding="0"][@border="0"]//tbody//td//input[@class="tB"]').click()

        all_time_elements = browser.find_elements(By.XPATH, '//div[@class="WdateDiv"]//div[@id="dpTime"]//table[@nowrap="nowrap"]//tbody//tr//td[@class="menu"]')

        for time_element in all_time_elements:
            t_element = time_element.text
            if t_element == arg_time:
                time_element.click()
                break

        time.sleep(2)
        browser.find_element(By.ID, 'dpOkInput').click()

    except Exception as e:
        logging.debug("Missing Element - Date From")
        logging.debug(e)
        return False
    else:
        logging.debug("Found - Date From\n")

    pbar.update(10)

    try:
        browser.switch_to.default_content()
        browser.switch_to.frame(browser.find_element(By.ID, 'mUrl'))
        browser.switch_to.frame(browser.find_element(By.ID, 'pageShowFrame'))
        browser.switch_to.frame(browser.find_element(By.ID, 'content-iframe'))
    except Exception as e:
        logging.debug("Problem - Switching frames")
        logging.debug(e)
        return False
    else:
        logging.debug("Switched Frames\n")



    try:
        time.sleep(10)
        end_date = browser.find_element(By.ID, 'endTime')
        end_date.click()

        browser.switch_to.default_content()
        logging.debug("Default Content\n")
        time.sleep(5)

        browser.switch_to.frame(browser.find_element(By.XPATH, '//div[@id="_my97DP"]//iframe[@src="http://truesecuritygps.net/My97DatePicker/My97DatePicker.htm"]'))
        logging.debug("Found Frame\n")

        time.sleep(2)
        all_dates = browser.find_elements(By.XPATH, '//div[@class="WdateDiv"]//table[@class="WdayTable"]//tbody//tr//td[@class="Wwday" or @class="Wday" or @class="WotherDay"]')

        for date_element in all_dates:
            date = date_element.text
            logging.debug(date)
            if date == arg_date:
                date_element.click()
                break

        time.sleep(2)
        browser.find_element(By.XPATH, '//div[@class="WdateDiv"]//div[@id="dpTime"]//table[@cellspacing="0"][@cellpadding="0"][@border="0"]//tbody//td//input[@class="tB"]').click()

        all_time_elements = browser.find_elements(By.XPATH, '//div[@class="WdateDiv"]//div[@id="dpTime"]//table[@nowrap="nowrap"]//tbody//tr//td[@class="menu"]')

        integer_list = []

        for time_element in all_time_elements:
            integer_list.append(int(time_element.text))

        if int(arg_time) in integer_list:
            for time_element in all_time_elements:
                t_element = time_element.text
                if t_element == arg_time:
                    time_element.click()
                    break
        else:
            for time_element in all_time_elements:
                t_element = time_element.text
                if t_element == str(max(integer_list)):
                    time_element.click()
                    break

        

        time.sleep(2)
        browser.find_element(By.ID, 'dpOkInput').click()
    except NoSuchElementException:
        logging.debug("Missing Element - Date To")
        return False
    else:
        logging.debug("Found - Date To\n")

    pbar.update(10)

    try:
        browser.switch_to.default_content()
        browser.switch_to.frame(browser.find_element(By.ID, 'mUrl'))
        browser.switch_to.frame(browser.find_element(By.ID, 'pageShowFrame'))
        browser.switch_to.frame(browser.find_element(By.ID, 'content-iframe'))
    except Exception as e:
        logging.debug("Problem - Switching frames")
        logging.debug(e)
        
        return False
    else:
        logging.debug("Switched Frames\n")


    try:
        query_btn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "searchBtn"))
        )
        time.sleep(10)
        query_btn = browser.find_element(By.ID, 'searchBtn')
        query_btn.click()
    except NoSuchElementException:
        logging.debug("Missing Element - Search Button")
        return False
    else:
        logging.debug("Found Search Button\n")

    try:
        excel_btn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "export"))
        )
        time.sleep(10)
        excel_btn = browser.find_element(By.ID, 'export')
        excel_btn.click()
    except NoSuchElementException:
        logging.debug("Missing Element - Export Button")
        return False
    else:
        logging.debug("Found Excel Button\n")

    pbar.update(10)
    pbar.close()
    print("\n")

    return True
