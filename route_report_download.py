import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from sqlalchemy import all_ 
browser = webdriver.Firefox()
browser.get('http://truesecuritygps.net/Skins/DefaultIndex_EN/')

userElem = browser.find_element_by_id('txtUserName')
userElem.send_keys('Truesecurity')
passwordElem = browser.find_element_by_id('txtPwd')
passwordElem.send_keys('TrueGPS123!')
passwordElem.submit()

try:
    monitoring_button = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Monitoring"))
    )
    time.sleep(10)
    monitoring_button.click()
except NoSuchElementException:
    print('Monitoring Link Missing')
    exit()
finally:
    print('Monitoring Link Found')
    


try:
    browser.switch_to.window(browser.window_handles[1])
except Exception as e:
    print('Failed to switch windows \n')
    print(e)
else:
    print('Switched Windows \n')


try:
    something = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, "mUrl"))
    )
    browser.switch_to.frame(browser.find_element_by_id('mUrl'))
except NoSuchElementException:
    print("Missing Frame")
    exit()
else:
    print("Found Frame\n")

try:
    time.sleep(60)
    report_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "goto_report"))
    )
    report_link = browser.find_element_by_id("goto_report")
    report_link.click()
except NoSuchElementException:
    print("Missing Element - Route Link")
    exit()
else:
    print("Found Route Link\n")

try:
    something = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, "pageShowFrame"))
    )
    browser.switch_to.frame(browser.find_element_by_id('pageShowFrame'))
except NoSuchElementException:
    print("Missing Frame 2")
    exit()
else:
    print("Found Frame 2\n")

try:
    time.sleep(10)
    rr_button = browser.find_element_by_link_text("Route report") 
    rr_button.click()
except NoSuchElementException:
    print('Missing Element - Route Link 2')
    exit()
else:
    print('Found Route Report Link\n')



try:
    something = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.ID, "custIframeTree"))
    )
    browser.switch_to.frame(browser.find_element_by_id('custIframeTree'))
except NoSuchElementException:
    print("Missing Frame 3")
    exit()
else:
    print("Found Frame 3\n")


try:
    plus_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "tree_3_switch"))
    )
    time.sleep(10)
    plus_button = browser.find_element_by_id('tree_3_switch')
    plus_button.click()
except NoSuchElementException:
    print("Missing Element - Plus Link Impala Terminals")
    exit()
else:
    print("Found Impala Terminals Link\n")

try:
    impala_button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "tree_9_span"))
    )
    time.sleep(10)
    impala_button = browser.find_element_by_id('tree_9_span')
    impala_button.click()
except NoSuchElementException:
    print("Missing Element - Plus Link Impala Trucks")
    exit()
else:
    print("Found Impala Trucks Link\n")


try:
    time.sleep(5)
    browser.switch_to.parent_frame()
    time.sleep(5)
    browser.switch_to.frame(browser.find_element_by_id('content-iframe'))
except NoSuchElementException:
    print("Missing Frame 4")
    exit()
else:
    print("Found Frame 4\n")

try:
    time.sleep(10)
    bg_date = browser.find_element_by_id('beginTime')
    bg_date.click()

    browser.switch_to.default_content()
    print("Default Content")
    time.sleep(5)

    browser.switch_to.frame(browser.find_element_by_xpath('//div[@id="_my97DP"]//iframe[@src="http://truesecuritygps.net/My97DatePicker/My97DatePicker.htm"]'))
    print("Found Frame")

    time.sleep(2)
    all_dates = browser.find_elements_by_xpath('//div[@class="WdateDiv"]//table[@class="WdayTable"]//tbody//tr//td[@class="Wwday" or @class="Wday" or @class="WotherDay"]')

    for date_element in all_dates:
        date = date_element.text
        print(date)
        if date == '27':
            date_element.click()
            break

    time.sleep(2)
    browser.find_element_by_xpath('//div[@class="WdateDiv"]//div[@id="dpTime"]//table[@cellspacing="0"][@cellpadding="0"][@border="0"]//tbody//td//input[@class="tB"]').click()

    all_time_elements = browser.find_elements_by_xpath('//div[@class="WdateDiv"]//div[@id="dpTime"]//table[@nowrap="nowrap"]//tbody//tr//td[@class="menu"]')

    for time_element in all_time_elements:
        t_element = time_element.text
        if t_element == '9':
            time_element.click()
            break

    time.sleep(2)
    browser.find_element_by_id('dpOkInput').click()

except Exception as e:
    print("Missing Element - Date From")
    print(e)
    exit()
else:
    print("Found - Date From\n")


try:
    browser.switch_to.default_content()
    browser.switch_to.frame(browser.find_element_by_id('mUrl'))
    browser.switch_to.frame(browser.find_element_by_id('pageShowFrame'))
    browser.switch_to.frame(browser.find_element_by_id('content-iframe'))
except Exception as e:
    print("Problem - Switching frames")
    print(e)
    exit()
else:
    print("Switched Frames\n")



try:
    time.sleep(10)
    bg_date = browser.find_element_by_id('endTime')
    bg_date.click()

    browser.switch_to.default_content()
    print("Default Content")
    time.sleep(5)

    browser.switch_to.frame(browser.find_element_by_xpath('//div[@id="_my97DP"]//iframe[@src="http://truesecuritygps.net/My97DatePicker/My97DatePicker.htm"]'))
    print("Found Frame")

    time.sleep(2)
    all_dates = browser.find_elements_by_xpath('//div[@class="WdateDiv"]//table[@class="WdayTable"]//tbody//tr//td[@class="Wwday" or @class="Wday" or @class="WotherDay"]')

    for date_element in all_dates:
        date = date_element.text
        print(date)
        if date == '29':
            date_element.click()
            break

    time.sleep(2)
    browser.find_element_by_xpath('//div[@class="WdateDiv"]//div[@id="dpTime"]//table[@cellspacing="0"][@cellpadding="0"][@border="0"]//tbody//td//input[@class="tB"]').click()

    all_time_elements = browser.find_elements_by_xpath('//div[@class="WdateDiv"]//div[@id="dpTime"]//table[@nowrap="nowrap"]//tbody//tr//td[@class="menu"]')

    for time_element in all_time_elements:
        t_element = time_element.text
        if t_element == '9':
            time_element.click()
            break

    time.sleep(2)
    browser.find_element_by_id('dpOkInput').click()
except NoSuchElementException:
    print("Missing Element - Date To")
    exit()
else:
    print("Found - Date To\n")


try:
    browser.switch_to.default_content()
    browser.switch_to.frame(browser.find_element_by_id('mUrl'))
    browser.switch_to.frame(browser.find_element_by_id('pageShowFrame'))
    browser.switch_to.frame(browser.find_element_by_id('content-iframe'))
except Exception as e:
    print("Problem - Switching frames")
    print(e)
    
    exit()
else:
    print("Switched Frames\n")


try:
    query_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "searchBtn"))
    )
    time.sleep(10)
    query_btn = browser.find_element_by_id('searchBtn')
    query_btn.click()
except NoSuchElementException:
    print("Missing Element - Search Button")
    exit()
else:
    print("Found Search Button\n")

try:
    excel_btn = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "export"))
    )
    time.sleep(10)
    excel_btn = browser.find_element_by_id('export')
    excel_btn.click()
except NoSuchElementException:
    print("Missing Element - Export Button")
    exit()
else:
    print("Found Excel Button\n")

exit()
