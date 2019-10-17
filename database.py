import sqlite3
conn = sqlite3.connect('passwordManager.db')

def createRecord(platform, link, username, password):
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

    else:
        record.execute('''
            INSERT INTO CREDENTIALS 
            (PLATFORM, LINK, USERNAME, PASSWORD)
            VALUES {platform},{link},{username},{password}
        ''')
        return 'RECORD ADDED'
    
def read(id):
    #this function takes in a record ID and returns a dictionary of all record fields
    
    #generate sql query
    #execute and put in dictionary 'result'
        #if any values are missing, replace them with None
    
    #if some error in reading
        #return false

    result = {"ID": 0, "platform": 'platform', "url": 'url', "username": 'username', "password": 'password'}
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
    #this function updates a record given all the parameters
    #create query string dynamically
    #execute query

    return True

def findAllRecords():
    c = conn.cursor()

    rows = c.execute('''
        SELECT * FROM CREDENTIALS 
    ''').fetchall()

    print(type(rows))

    #temporary return, return format example
    result = {"LifeLock": 1, "BankOfAmerica": 2, "Charles Schwab": 3, "Credit Karma": 4, "Reddit": 5}
    return result

findAllRecords()