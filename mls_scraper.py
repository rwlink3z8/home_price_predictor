import requests
from bs4 import BeautifulSoup
import pprint
'''
_ct10_m_hfKeys - this is the input tag with the id
the entire list of listings is available in the entire html, this pulls all the listing information into a list of key value pairs
'''

session = requests.Session()
r = session.get("https://matrix.heartlandmls.com/Matrix/Public/Portal.aspx?k=990316X949Z&p=DE-77667588-490")
soup = BeautifulSoup(r.content, "lxml")

keys = soup.find("input",{"id":"_ctl0_m_hfKeys"})["value"]
did = session.cookies.get_dict()["Display"]

r = requests.post("https://matrix.heartlandmls.com/matrix/public/getdisplay/ByKeys.ashx",
  params = {
    "drm": "email"
  },
  data = {
    "keys": keys,
    "did": did,
    "tid": 1,
    "l": 1,
    "pbs": 1
   })
soup = BeautifulSoup(r.content, "lxml")

items = []

for i in soup.find_all("div",{"class":"multiLineDisplay"}):
  span = i.find_all("span")
  item = {
    "image": span[0].find("img")["src"],
    "price": span[1].text,
    "status1": span[4].text,
    "status2": span[5].text,
    "address1": span[6].text,
    "address2": span[7].text,
    "bedroomNum": span[8].text,
    "FullBathroomNum": span[10].text,
    "HalfBathroomNum": span[12].text,
    "sqft": span[14].text,
  }
  if (len(span)>20):
    item["builtIn"] = span[17].text
    item["acres"] = span[18].text
    item["family"] = span[20].text
    item["description"] = span[21].text
  elif (len(span)>19):
    item["builtIn"] = span[17].text
    item["family"] = span[18].text
    item["description"] = span[19].text
  else:
    item["family"] = span[15].text
    item["description"] = span[16].text
  items.append(item)
