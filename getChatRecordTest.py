import getChatRecord


#loading chat page
urlOfLoadPage="https://www.youtube.com/live_chat?v=QARPzMkjcCg&is_popout=1"
try:
    getChatRecord.connect(5,urlOfLoadPage)
except:
    print("load error")
rowOfNewTable=0
while(True):
    try:
        newRecordTable=getChatRecord.loadRecord()
    except:
        print("get content error")
    try:
        rowOfNewTable=len(newRecordTable)
    except:
        print("error")
   
    for i in range(rowOfNewTable):
        print(newRecordTable[i])