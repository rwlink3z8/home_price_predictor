

'''
The big thing here is we are finding a unique way to get the element and clicking it.
This post has some stuff on it unfortunately I dont think it is in python.
https://stackoverflow.com/questions/52405456/selenium-how-to-click-on-javascript-button
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://matrix.heartlandmls.com/Matrix/Public/Portal.aspx?L=1&k=990316X949Z&p=DE-74613894-421"
h_table = []
driver = webdriver.Firefox()
driver.get(url)
# xpath that clicks on the first listing, expanding the features of listing, this is the JS doPostBack function 
driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div[5]/div[3]/span[2]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/span/a").click()
time.sleep(10)
while True:
    if len(h_table) >= 200:
        print('done')
        break
    else:
        #wrapper table appends everything from each listing, this will need to be cleaned up quite a bit before modelling
        h_table.append(driver.find_element_by_id("wrapperTable").text)
        #xpath for the next listing button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/div/div[5]/div[2]/div/div[1]/div/div/span/ul/li[2]/a'))).click()
