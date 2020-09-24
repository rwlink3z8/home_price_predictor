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
