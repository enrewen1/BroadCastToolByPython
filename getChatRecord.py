
import os,time
from selenium import webdriver

driverPath = os.getcwd() + '/chromedriver'
browser = webdriver.Chrome(driverPath)
NumberOfPosts=0

def connect(timeForFirstLoad=5,urlOfLoadPage="www.google.com"):
         
    browser.get(urlOfLoadPage)
    time.sleep(timeForFirstLoad)

def loadRecord():

    nameList=browser.find_elements_by_class_name('yt-user-name')
    lengthOfList=len(nameList)
    recordList=[]
    global NumberOfPosts
    if(lengthOfList>NumberOfPosts):
        listcomment=browser.find_elements_by_class_name('comment-text')
        for i in range(lengthOfList-NumberOfPosts):
            recordList.append(nameList[-lengthOfList+NumberOfPosts+i].text+":"+listcomment[-lengthOfList+NumberOfPosts+i].text)
        NumberOfPosts=lengthOfList
        
        return recordList
    
    
    #browser.quit() # 關閉 chromedriver

