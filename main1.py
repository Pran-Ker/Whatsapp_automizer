import datetime
import json
from selenium import webdriver
import time


def wish_birth(name):
    return "Happy Birthday " + name.split(" ")[0] + "!!"

def getJsonData(file,attr_ret,attr1,attr2,attr_val1,attr_val2):
    data = json.load(file)
    retv=[]
    #return data
    for i in data:
        if(i[attr1]==attr_val1 and i[attr2]==attr_val2):
           retv.append(i[attr_ret])
    return retv


datt=datetime.datetime.now()

data_file=open("birthdays.json","r")
# print(datt.month,datt.day)
namev=[]
while True:
    #print("here")
    try:
        namev=getJsonData(data_file,"name","birth_month","birth_date",str(datt.month),str(datt.day))
    except json.decoder.JSONDecodeError:
        continue
    if(namev!=[]):
        break
chropt=webdriver.ChromeOptions()

chropt.add_argument("user-data-dir=<***USER DATA DESTINATION GOES HERE***>")

driver=webdriver.Chrome(executable_path="<***WEB DRIVER PATH HERE***",options=chropt)
driver.get("https://web.whatsapp.com/")
time.sleep(3)
print(namev)
#input("Scan Now")
for inp in namev:
    eleNM=driver.find_element_by_xpath('//span[@title="{}"]'.format(inp))
    eleNM.click()

    while(True):
        # latestmsg=driver.find_element_by_class_name("selectable-text invisible-space copyable-text").get_attribute("span")
        # print(str(latestmsg))
        eleTF=driver.find_element_by_class_name("_13mgZ")
        eleTF.send_keys(wish_birth(inp))
        eleSND=driver.find_element_by_class_name("_3M-N-")
        eleSND.click()
        break
