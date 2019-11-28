import sqlite3
import math

def createRecord(platform, link, username, password):
    #create the connection
    conn = sqlite3.connect('passwordManager.db')
    record = conn.cursor()

    myId = 

    #consolidate the values
    values = (myId, platform, link, username, password)

    #check for errors
    if not platform:
        return "HEY DUDE, YOU HAVE TO TYPE IN A PLATFORM"
    elif not link:
        return "HEY DUDE, YOU HAVE TO TYPE IN A LINK"
    elif not username:
        return "HEY DUDE, YOU HAVE TO TYPE IN A USERNAME"
    elif not password:
        return "HEY DUDE, YOU HAVE TO TYPE IN A PASSWORD"

    #execute the statement
    else:
        sqlstring = '''INSERT INTO CREDENTIALS VALUES(?, ?, ?, ?, ?)'''
        record.execute(sqlstring, values)
        if record.rowcount:
            return 'success!'
        return 'fail'
    
def read(id):
    conn = sqlite3.connect('passwordManager.db')
    #this function takes in a record ID and returns a dictionary of all record fields
    
    #generate sql query
    #execute and put in dictionary 'result'
        #if some error in reading
            #return false
        #if any values are missing, replace them with None

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
    #this function deletes a record given an ID

    #create query string dynamically

    #execute query

    #if error
        #return False

    #otherwise
    return True

def findAllRecords():
    #create the connection
    conn = sqlite3.connect('passwordManager.db')
    c = conn.cursor()

    rows = c.execute('''
        SELECT * FROM CREDENTIALS 
    ''').fetchall()

    print(c.rowcount())

    print(type(rows))
    print(rows)

    conn.close()

    #temporary return, return format example
    #result = {"LifeLock": 1, "BankOfAmerica": 2, "Charles Schwab": 3, "Credit Karma": 4, "Reddit": 5}
    return #result

if __name__ == "__main__":
    print(createRecord("LifeLock", "www.lifelock.com", "username", "hunter2"))
    print(createRecord("Hackerrank", "www.hackerrank.com", "hacker", "password"))
    print(createRecord("CoinBase", "www.coinbase.com", "Mr. Robot", "cryptoPassword"))
    findAllRecords()
