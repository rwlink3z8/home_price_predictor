from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.common import exceptions

'''
this is a webscraper for scraping the entirety of each MLS listing with selenium, webdriver wait sped the scraper up significantly as opposed to just setting a sleep timer
one weird behavior I have noticed is that it sometimes clicks and adds duplicates, so I had it go an extra 10-15% of all entries to account for that

the scraper opens the MLS listing main page
then it clicks the first listing and grabs the wrapper table from each listing and clicks on the next listing
'''



url= "https://matrix.heartlandmls.com/Matrix/Public/Portal.aspx?L=1&k=990316X949Z&p=DE-77667588-490"                                                                          
new_set5001 = []
ignored_exceptions = [exceptions.NoSuchElementException, exceptions.StaleElementReferenceException, exceptions.WebDriverException]
driver = webdriver.Firefox()
driver.get(url)
driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div[5]/div[3]/span[2]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/span/a").click()
time.sleep(5)
# 500 total listings on this site but the scraper has some behavior i can't explain
while True:
    if len(new_set5001)>=570:
        print('done')
        break
    else:
        try:
            new_set5001.append(driver.find_element_by_id("wrapperTable").text)
            WebDriverWait(driver, 20, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[3]/div/div/div[5]/div[2]/div/div[1]/div/div/span/ul/li[2]/a"))).click()
        except (exceptions.NoSuchElementException, exceptions.StaleElementReferenceException) as err:
            time.sleep(15)
