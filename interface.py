from tkinter import *
import pyperclip as pc

#from database import *

def getPlatforms(category):
    #given a category, get a list of platforms in that category
    return

def updateInfo(platform, link, username, password):
    #with new info, update all the fields
    return

def deleteInfo():
    #check to confirm you want to delete
    #look up the platform ID
    #delete from table
    return

def getID(platform):
    # ID = 0
    #query database to get id matching platform
    return 

def createRecord(platform, link, username, password):
    #check to see if platform already exists
    #throw error if so
    #execute create query
    return

#TK is the window
#Label for lables
#Button for buttons
#Entry for inputBox
class mainMenu:
    def __init__(self, window):
        #create the main window and attributes
        self.window = window
        self.window.title("Password Manager")
        
        #set dimensions
        self.width = 370
        self.height = 165

        #position center and north a bit
        self.xPosition = int(window.winfo_screenwidth() / 2 - self.width / 2)
        self.yPosition = int(window.winfo_screenheight() / 2 - self.height / 0.8) 
        window.geometry(f'{self.width}x{self.height}+{self.xPosition}+{self.yPosition}')

        #initialize variables
        self.platform = 'platform'
        self.url = 'url'
        self.username = 'username'
        self.password = 'password'

        #create the labels
        self.mainPlatformLabel = Label(window, text="Load Data: ")
        self.mainPlatformLabel.grid(column=0, row=0, sticky=W)
        self.platformLabel = Label(self.window, text="Platform: ")
        self.platformLabel.grid(column=0, row=1, sticky=W)
        self.linkLabel = Label(self.window, text="Link: ")
        self.linkLabel.grid(column=0, row=2, sticky=W)
        self.usernameLabel = Label(self.window, text="Username: ")
        self.usernameLabel.grid(column=0, row=3, sticky=W)
        self.passwordLabel = Label(self.window, text="Password: ")
        self.passwordLabel.grid(column=0, row=4, sticky=W)

        #create the dropdown
        self.platforms = {"LifeLock", "BankOfAmerica", "Charles Schwab", "Credit Karma", "Reddit"}
        self.platformVar = StringVar(self.window)
        self.platformVar.set('LifeLock')
        self.platformMenu = OptionMenu(self.window, self.platformVar, *self.platforms)
        self.platformMenu.config(width='28')
        self.platformMenu.grid(column=1, row=0)

        #and fields boxes
        self.platformBox = Entry(self.window, width=30)
        self.platformBox.grid(column=1, row=1)
        self.linkBox = Entry(self.window, width=30)
        self.linkBox.grid(column=1, row=2)
        self.usernameBox = Entry(self.window, width=30)
        self.usernameBox.grid(column=1, row=3)
        self.passwordBox = Entry(self.window, width=30)
        self.passwordBox.grid(column=1, row=4)

        #create the button frames
        self.buttonFrame = Frame(self.window)
        self.buttonFrame.grid(column=0, row=5, columnspan=2)

        #create the buttons
        self.getDataBtn = Button(self.buttonFrame, text="Get Info", command=self.getData)
        self.getDataBtn.config(width='7')
        self.getDataBtn.grid(column=0, row=0)

        self.goButton = Button(self.buttonFrame, text = 'Go', command=self.go)
        self.goButton.config(width='7')
        self.goButton.grid(column=1, row=0, sticky=W)

        self.updateButton = Button(self.buttonFrame, text = 'Update', command=self.update)
        self.updateButton.config(width='8')
        self.updateButton.grid(column=2, row=0, sticky=W)

        self.addButton = Button(self.buttonFrame, text = 'Add', command=self.add)
        self.addButton.config(width='8')
        self.addButton.grid(column=3, row=0, sticky=W)

        self.deleteButton = Button(self.buttonFrame, text = 'Delete', command=self.delete)
        self.deleteButton.config(width='8')
        self.deleteButton.grid(column=4, row=0, sticky=W)

        

        #add Go button that opens the site and copies password onto the clipboard
    
    def getData(self):
        print(self.platformVar.get())
        #get the info into a list
        self.passwordBox.insert(0, self.password)
        self.usernameBox.insert(0, self.username)
        self.linkBox.insert(0, self.url)
        self.platformBox.insert(0, self.platform)

        return

    def update(self):
        print('update called')
        return
    
    def add(self):
        print('add called')
        return

    def delete(self):
        print('delete called')
        return

    def go(self):
        print('go called')
        return

    

    
# class messageBox:
#     __init__(self, window, message):



if __name__=="__main__":
    root = Tk()
    app = mainMenu(root)
    root.mainloop()





