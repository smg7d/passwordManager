import sqlite3
conn = sqlite3.connect('passwordManager.db')
c = conn.cursor()

def createRecord(platform, link, username, password):
    #generate an id
    #generate sql query
    #execute query

    return True
    
def read(id):
    result = {}
    #generate sql query
    #execute and put in dictionary 'result'

    return result

def updateRecord(id, col, val):
    #this function updates a record given all the parameters
    #create query string dynamically
    query_string = f'update ({col}) where id = {id} VALUES (val);'
    #execute query

    return True

def deleteRecord(id):
    #this function updates a record given all the parameters
    #create query string dynamically
    #execute query

    return True