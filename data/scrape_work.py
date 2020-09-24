'''
If your issue is because it is a hidden java element (to keep people from scraping) it most likely has code like below
'''
<input type="hidden" name="ctl00$body$grdSalesSummary$ctl04$hdnCommCode" id="ctl00_body_grdSalesSummary_ctl04_hdnCommCode" value="59">
<a id="ctl00_body_grdSalesSummary_ctl04_lnkParcelID" href="javascript:__doPostBack('ctl00$body$grdSalesSummary$ctl04$lnkParcelID','')" style="font-weight: bold; text-decoration: underline; cursor: pointer; color: Black;">0594080000000160</a>
'''
The first tag is before the second which is a link to the next page I wanted however it was 'hidden' until it was moused over.  You should be able to do something like the code below to click it
'''


driver.find_element_by_xpath(
        '//*[@id="ctl00_body_grdSalesSummary_ctl{0:02d}_lnkParcelID"]').click()

'''
The big thing here is we are finding a unique way to get the element and clicking it.
This post has some stuff on it unfortunately I dont think it is in python.
https://stackoverflow.com/questions/52405456/selenium-how-to-click-on-javascript-button
finally below is the code I helped a student with.  (not sure if any of this is helpful)
'''

# Selenium to get to parcels
for b_date, e_date in zip(beginning_date, end_date):
    driver = webdriver.Firefox()
    time.sleep(3)
    driver.get('http://epas.csc-ma.us/PublicAccess/Pages/AllCommunitySearchSales.aspx') 
    time.sleep(3)
    date1 = driver.find_element_by_name("ctl00$body$txtSalesDateRange")
    date1.send_keys(b_date)
    time.sleep(2)
    date2 = driver.find_element_by_name("ctl00$body$txtSalesDateRangeTo")
    date2.send_keys(e_date)
    city = driver.find_element_by_name("ctl00$body$txtCommunity")
    city.send_keys("Needham")
    time.sleep(2)
    find_button = driver.find_element_by_name("ctl00$body$btnFind")
    find_button.click()
    time.sleep(5)
    for i in range(3,53):
        # Get the link object to click
        #
        # This is the point where I click and get the new page.  
        # I found the path using inspect on the element and just put it there 
        # The main thing is I find the element that is supposed to be clicked and clickit.
        #
        link = driver.find_element_by_xpath(
        '//*[@id="ctl00_body_grdSalesSummary_ctl{0:02d}_lnkParcelID"]'.format(i))
        link.click()
        time.sleep(10)
        # Gather what you need here 
        print(i)
        # Go back and go to the next page
        driver.back()
        time.sleep(10)
        
        
  # scraper 3 example
from selenium import webdriver
import pandas as pd


url = "https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/#/page/{}/"

def scrape_odds_portal(url):
    #instantiate an automated browser
    browser = webdriver.Chrome()
    browser.get(url)
    # get the sources of the page
    df= pd.read_html(browser.page_source, header=0)[0]
    # we are interested in dates, matchups, and moneylines for each team
    dateList = [] 
    gameList = [] #row[2]
    money_line1List = [] #row[5]
    money_line2List = [] # row[6]

    for row in df.itertuples():
        if not isinstance(row[1], str):
            continue
        elif ':' not in row[1]:
            date = row[1].split('-')[0]
            continue
        time = row[1]
        dateList.append(date)
        gameList.append(row[2])
        money_line1List.append(row[5])
        money_line2List.append(row[6])

    result = pd.DataFrame({'date':dateList,
                       'game':gameList,
                       'money_line1':money_line1List,
                       'money_line2':money_line2List})

    return result

#stackoverflow answer to my question
from selenium import webdriver
import pandas as pd

browser = webdriver.Chrome()
browser.get("https://www.oddsportal.com/american-football/usa/nfl-2017-2018/results/")

df= pd.read_html(browser.page_source, header=0)[0]

dateList = []
gameList = []
money_line1List = []
money_line2List = []

for row in df.itertuples():
    if not isinstance(row[1], str):
        continue
    elif ':' not in row[1]:
        date = row[1].split('-')[0]
        continue
    time = row[1]
    dateList.append(date)
    gameList.append(row[2])
    money_line1List.append(row[5])
    money_line2List.append(row[6])

result = pd.DataFrame({'date':dateList,
                       'game':gameList,
                       'money_line1':money_line1List,
                       'money_line2':money_line2List})

'''
https://towardsdatascience.com/create-a-model-to-predict-house-prices-using-python-d34fe8fad88f

this has a good visualization tool for where houses are located 

https://www.deploymachinelearning.com/

good website for deploying machine learning models
'''

'''
button information for the
first and
second listing

'''
from selenium import webdriver
import pandas as pd

element: (outer html)
<a href="javascript:__doPostBack('_ctl0$m_DisplayCore','Redisplay|4526,,0')">403 W  Main Street</a>
<a href="javascript:__doPostBack('_ctl0$m_DisplayCore','Redisplay|4526,,1')">600  Lake Road</a>
<a href="javascript:__doPostBack('_ctl0$m_DisplayCore','Redisplay|4526,,2')">83  Spruce Street</a>

css selector:
div.multiLineDisplay:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)

div.multiLineDisplay:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1) > a:nth-child(1)

css path:
html body.mtx-body form#ctl01.j-modalAttachTarget div#m_pnlPortalContent.container-fluid div.row div.col-xs-12 div#_ctl0_m_pnlTop div#_ctl0_m_divResultsContent.row.j-resultsContent span#_ctl0_m_upResults div#_ctl0_m_pnlResults div#_ctl0_m_pnlRenderedDisplay.col-xxs-12.col-xs-6.j-resultsColumnDisplays.mtx-resultsColumnForDisplays div#_ctl0_m_divAsyncPagedDisplays.j-resultsPageAsyncDisplays div.multiLineDisplay.ajax_display.d4528m_show div#wrapperTable.d-wrapperTable div.row.d-paddingTop--6.d-paddingBottom--6.d-bgcolor--systemLightest.d-marginBottom--4.d-marginLeft--4.d-marginRight--4.d-marginTop--4 div.col-lg-7.col-md-6.col-sm-12 div.row div.col-sm-12.d-fontSize--largest.d-text.d-color--brandDark span.formula.J_formula a

xpath:
/html/body/form/div[3]/div/div/div[5]/div[3]/span[2]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/span/a
/html/body/form/div[3]/div/div/div[5]/div[3]/span[2]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/span/a
/html/body/form/div[3]/div/div/div[5]/div[3]/span[2]/div/div/div[2]/div[3]/div/div/div[2]/div[2]/div[1]/span/a


url = "https://matrix.heartlandmls.com/Matrix/Public/Portal.aspx?k=990316X949Z&p=DE-77667588-490"

browser = webdriver.Chrome()
browser.get(url)
browser.find_element_by_xpath("/html/body/form/div[3]/div/div/div[5]/div[3]/span[2]/div/div/div[2]/div[1]/div/div/div[2]/div[2]/div[1]/span/a")
