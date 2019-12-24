from tkinter import *
import pyperclip
import database as db

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
        self.platform = '' #this stores the 'current' platform
        self.url = '' #this stores the 'current' url
        self.username = '' #this stores the 'current' username
        self.password = '' #this stores the 'current' password
        self.platforms = db.getPlatforms() #this gets a list of all platforms
        self.platformVar = StringVar(self.window) #this is how you interact with the dropdown box program-wise

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

    def getInfo(self):

        #get the object from the database and update fields
        try:
            itemID = str(self.platformVar.get())
            newObj = db.read(itemID)
            self.platform = newObj.platform
            self.url = newObj.link
            self.username = newObj.username
            self.password = newObj.password
        except:
            #if except, alert and exit
            self.alertUser(f'''Could not find {itemID} in 
database. Try adding it.''')
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
        #create a new platform object and populate data from interface
        platformToUpdate = db.Platform()
        platformToUpdate.platform = self.platformBox.get()
        platformToUpdate.link = self.linkBox.get()
        platformToUpdate.username = self.usernameBox.get()
        platformToUpdate.password = self.passwordBox.get()

        #alert and exit if no platform selected
        if not platformToUpdate.platform:
            self.alertUser('''No platform selected. Make sure a 
valid platform is selected and try again''')
            return

        #call the update function and put its results to the screen
        try:
            self.alertUser(db.update(platformToUpdate))
        except:
            self.alertUser('''Invalid input. Make sure a valid platform
is selected and try again''')

        return
    
    def add(self):
        #create a new platform object and populate data from interface
        platformToAdd = db.Platform()
        platformToAdd.platform = self.platformBox.get()
        platformToAdd.link = self.linkBox.get()
        platformToAdd.username = self.usernameBox.get()
        platformToAdd.password = self.passwordBox.get()

        try:
            self.alertUser(db.create(platformToAdd))
            self.refreshPlatformMenu()
        except:
            self.alertUser(f'''Could not add "{platformToAdd.platform}".
Re-enter data and try again.''')

        return

    def delete(self):
        #get platform, ID
        try:
            platform = self.platformBox.get()

            if not platform or (platform not in self.platforms):
                self.alertUser('''Invalid platform. Select
a platform and try again''')
                return
            self.alertUser(db.delete(platform))
            self.platformVar.set('Select a platform')
            self.passwordBox.delete(0, END)
            self.usernameBox.delete(0, END)
            self.linkBox.delete(0, END)
            self.platformBox.delete(0, END)
            self.refreshPlatformMenu()
        except:
            self.alertUser(f'''Could not delete {platform}
Re-enter data and try again.''')

        return

    def go(self):

        #copies password to clipboard
        pyperclip.copy(self.passwordBox.get())

        #opens selenium browser to website

        return

    def alertUser(self, message):
        self.newWindow = Toplevel(self.window)
        self.alertBox = messageBox(self.newWindow, message)

    def refreshPlatformMenu(self):
        #erase current menu options 
        menu = self.platformMenu['menu']
        menu.delete(0, 'end')

        print("in here")
        #populate menu options based on db platforms
        self.platforms = db.getPlatforms()
        for p in self.platforms:
            menu.add_command(label=p, 
                             command=lambda value=p: self.platformVar.set(value))

        self.platformVar.set('Select a platform')
        return

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





