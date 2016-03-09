import getChatRecord


#loading chat page
urlOfLoadPage="https://www.youtube.com/live_chat?v=QARPzMkjcCg&is_popout=1"
getChatRecord.connect(5,urlOfLoadPage)
rowOfNewTable=0
while(True):
    newRecordTable=getChatRecord.loadRecord()
    try:
        rowOfNewTable=len(newRecordTable)
    except:
       continue
    for i in range(rowOfNewTable):
        print(newRecordTable[i])