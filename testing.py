import tkinter as tk # Python 3
import tkinter.scrolledtext as tkst
import getChatRecord

class Test():
    def getNewMessage(self,parent,editArea):
        
        rowOfNewTable=0
        newRecordTable=getChatRecord.loadRecord()
        try:
            rowOfNewTable=len(newRecordTable)
            for i in range(rowOfNewTable):
                
                editArea.insert(tk.END,newRecordTable[i]+"\n")
                editArea.see(tk.END)
        except:
            print("no new message")
            
  
        parent.update()
        
    def setWindowView(self,mainWindow,title,):
        mainWindow.title(title)
        mainWindow.wm_attributes('-topmost',1)
        mainWindow.attributes('-alpha', 1)   
        
    def setEditArea(self,parent):
        
        editArea = tkst.ScrolledText(
        master = parent,
        wrap   = tk.WORD,
        width  = 20,
        height = 10,
        
        )
        editArea.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        return editArea
    def enterKey(self,a):
        print("pressed enter")
        print(a.get())
        getChatRecord.sendMessage(a.get())
        a.delete(0,"end")
    
tool =Test()
root = tk.Tk()


tool.setWindowView(root,"YOGA版聊天室")

editAreaParent=root
editArea = tool.setEditArea(editAreaParent)

a=tk.Entry(bd=5)
a.pack(fill=tk.X)


root.bind('<Return>',(lambda event: tool.enterKey(a)))





#loading chat page
urlOfLoadPage="https://www.youtube.com/live_chat?v=QARPzMkjcCg&is_popout=1"
getChatRecord.connect(5,urlOfLoadPage)


while True:
   
    tool.getNewMessage(root,editArea)
    
    


root.mainloop()