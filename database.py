import sqlite3


def createRecord(platform, link, username, password):
    conn = sqlite3.connect('passwordManager.db')
    #generate an id
    #generate sql query
    #execute query
    record = conn.cursor()

    if not platform:
        return "HEY DUDE, YOU HAVE TO TYPE IN A PLATFORM"
    elif not link:
        return "HEY DUDE, YOU HAVE TO TYPE IN A LINK"
    elif not username:
        return "HEY DUDE, YOU HAVE TO TYPE IN A USERNAME"
    elif not password:
        return "HEY DUDE, YOU HAVE TO TYPE IN A PASSWORD"

    #to do, fix this query so that it works
    else:
        record.execute('INSERT INTO CREDENTIALS (PLATFORM, LINK, USERNAME, PASSWORD) VALUES (?, ?, ?, ?)', (platform, link, username, password))
        conn.close()
        return 'RECORD ADDED' 
    
def read(id):
    conn = sqlite3.connect('passwordManager.db')
    #this function takes in a record ID and returns a dictionary of all record fields
    
    #generate sql query
    #execute and put in dictionary 'result'
        #if some error in reading
            #return false
        #if any values are missing, replace them with None
    
    conn.cursor.execute('select from CREDENTIALS where id = ?', id)
    arr = conn.fetchone()
    result = {"ID": arr[0], "platform": arr[1], "url": arr[2], "username": arr[3], "password": arr[4]}
    conn.close()
    return result

def updateRecord(platform, url, username, password, itemID):
    #this function updates a record given all the parameters
    #create query string dynamically
    query_string = f'update (PLATFORM, URL, USERNAME, PASSWORD) where id = {itemID} VALUES ({platform}, {url}, {username}, {password});'
    #execute query
    print(query_string)
    #if exectution is successful, return string "update successful!"
    #if not, return the error message
    return f'Update for {platform} successful!'

def deleteRecord(id):
    #this function deletes a record given an ID

    #create query string dynamically

    #execute query

    #if error
        #return False

    #otherwise
    return True

def findAllRecords():
    conn = sqlite3.connect('passwordManager.db')
    c = conn.cursor()

    c.execute('SELECT * FROM CREDENTIALS')
    rows = c.fetchall()

    #temporary return, return format example
    result = {}
    print(rows)

    return result

createRecord('Charles Schwab','www.charlesschwab.com','notauser','notapassword')
findAllRecords()