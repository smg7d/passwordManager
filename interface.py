from tkinter import *
import pyperclip as pc
import database

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
        self.platform = ''
        self.url = ''
        self.username = ''
        self.password = ''
        self.platforms = database.findAllRecords()
        self.platformVar = StringVar(self.window)

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
        self.platformVar.set('Select a platform')
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

        #create the button frame
        self.buttonFrame = Frame(self.window)
        self.buttonFrame.grid(column=0, row=5, columnspan=2)

        #create the buttons
        self.getDataBtn = Button(self.buttonFrame, text="Get Info", command=self.getInfo)
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
    
    def updateData(self):
        #get the ID for the selected platform, return None if the platform is not in the dictionary
        itemID = self.platforms.get(str(self.platformVar.get()), None)

        #check if the resulting ID is valid and if not, return without taking action
        if itemID == None:
            self.alertUser('You must select a valid platform \n before proceeding')
            return False

        #get the data from the database
        newData = database.read(itemID)

        #update class variables with results from query
        self.platform = newData.get("platform", "-")
        self.url = newData.get("url", "-")
        self.username = newData.get("username", "-")
        self.password = newData.get("password", "-")

        #return success
        return True

    def getInfo(self):
        #update data based on the platform selected. if the query failed, return without action
        if not self.updateData():
            return

        #delete the current values
        self.passwordBox.delete(0, END)
        self.usernameBox.delete(0, END)
        self.linkBox.delete(0, END)
        self.platformBox.delete(0, END)

        #put the updated info into the appropriate boxes
        self.passwordBox.insert(0, self.password)
        self.usernameBox.insert(0, self.username)
        self.linkBox.insert(0, self.url)
        self.platformBox.insert(0, self.platform)

        return

    def update(self):
        
        #get all the of the fields in the boxes and put them in variables
        platform = self.platformBox.get()
        url = self.linkBox.get()
        username = self.usernameBox.get()
        password = self.passwordBox.get()
        itemID = self.platforms.get(platform, None)

        #check to make sure none of them are invalid
        if not (platform and url and username and password and itemID):
            self.alertUser('''Invalid input. Make sure each box is
filled out and the platform box 
matches an existing platform.''')
            return

        #call the update function and put its results to the screen
        self.alertUser(database.updateRecord(platform, url, username, password, itemID))
        return
    
    def add(self):
        #get data in all of the fields
        #validate the data
        #confirm that they would like to create a new record
        #execute query
        self.alertUser('Add called')
        return

    def delete(self):
        #validate platform maps to a valid ID
        #confirm that they would like to delete the record.
        #if so, execute the query
        self.alertUser('Delete called')
        return

    def go(self):
        self.alertUser('Go called')

        #copies password to clipboard
        #opens selenium browser to website

        return

    def alertUser(self, message):
        self.newWindow = Toplevel(self.window)
        self.alertBox = messageBox(self.newWindow, message)

class messageBox:
    def __init__(self, window, message):
        self.window = window
        self.window.title('Message')

        #set dimensions
        self.width = 250
        self.height = 80

        #position center and north a bit
        self.xPosition = int(window.winfo_screenwidth() / 2 - self.width / 2)
        self.yPosition = int(window.winfo_screenheight() / 2 - self.height / 0.8) 
        window.geometry(f'{self.width}x{self.height}+{self.xPosition}+{self.yPosition}')

        #configure rows and column to center
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=1)

        #create the label
        self.messageLabel = Label(self.window, text=message)
        self.messageLabel.grid(column=0,row=0)

        #create the button
        self.okButton = Button(self.window, text="OK", command=self.close_window)
        self.okButton.config(width='5', height='1')
        self.okButton.grid(column=0, row=1)

    def close_window(self):
        self.window.destroy()

if __name__=="__main__":
    root = Tk()
    app = mainMenu(root)
    root.mainloop()





