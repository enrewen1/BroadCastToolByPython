import tkinter as tk # Python 3
import tkinter.scrolledtext as tkst
import getChatRecord
import threading
from turtledemo.nim import COLOR
from selenium.webdriver.support.color import Color




class Test():
    def getNew(self,parent):
        
        rowOfNewTable=0
        newRecordTable=getChatRecord.loadRecord()
        try:
            rowOfNewTable=len(newRecordTable)
            for i in range(rowOfNewTable):
                
                editArea.insert(tk.END,newRecordTable[i]+"\n")
                editArea.see(tk.END)
        except:
            print("error")
  
        parent.update()
        
        
        
     

root = tk.Tk()
root.title("YOGA版聊天室")
root.wm_attributes('-topmost',1)
#root.attributes('-alpha', 0.1)   
editArea = tkst.ScrolledText(
        master = root,
        wrap   = tk.WORD,
        width  = 20,
        height = 10,
        
        )

editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)




#loading chat page
urlOfLoadPage="https://www.youtube.com/live_chat?v=QARPzMkjcCg&is_popout=1"
getChatRecord.connect(5,urlOfLoadPage)

tool =Test()
while True:
    tool.getNew(root)
#root.after(1,tool.getNew(root))
root.mainloop()