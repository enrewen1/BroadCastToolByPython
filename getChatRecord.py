
import os, time
from selenium import webdriver

driverPath =os.getcwd() + '/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/LoveYoplus/AppData/Local/Google/Chrome/User Data")
browser = webdriver.Chrome(executable_path=driverPath,chrome_options=options)

NUMBEROFPOSTS = 0
# connect to Page and set the load time,load page
def connect(timeForFirstLoad=5, urlOfLoadPage="www.google.com"):
    
    browser.get(urlOfLoadPage)
    time.sleep(timeForFirstLoad)

def loadRecord():
    className=["yt-user-name","comment-text","author"]
    commentList = browser.find_elements_by_class_name(className[1])
    lengthOfList = len(commentList)
    recordList = []
    global NUMBEROFPOSTS
    if(lengthOfList > NUMBEROFPOSTS):
        nameList = browser.find_elements_by_class_name(className[0])
        for i in range(lengthOfList - NUMBEROFPOSTS):
            recordList.append(nameList[-lengthOfList + NUMBEROFPOSTS + i].text + ":" + commentList[-lengthOfList + NUMBEROFPOSTS + i].text)
        NUMBEROFPOSTS = lengthOfList
        
        return recordList
    
def sendMessage(text):
    element = browser.find_element_by_id("live-comments-input-field")
    element.send_keys(text)
    element.submit()
    # browser.quit() # 關閉 chromedriver

