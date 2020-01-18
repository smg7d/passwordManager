import sqlite3, os, math, sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#check if database exists and if not, create new one
try:
    con = sqlite3.connect('file:passwordManager.db?mode=rw', uri=True)
except sqlite3.Error:
    print('passwordManager.db database not found. creating a new one')
    con = sqlite3.connect('passwordManager.db')
    c = con.cursor()
    c.execute('''CREATE TABLE logInData (
        platform text PRIMARY KEY,
        link text,
        username text,
        password text);
        ''')
    con.commit()
    con.close()

#declare the class
Base = declarative_base()
class Platform(Base):
    __tablename__ = 'logInData'
    platform = Column(String(250), primary_key = True)
    link = Column(String(250), nullable=True)
    username = Column(String(250), nullable=True)
    password = Column(String(250), nullable=True)

#auto-get info on dropdown change. delete "get info" button
#bind to executable to be shared


#set up the session factory
engine = create_engine('sqlite:///passwordManager.db')
DBSession = sessionmaker(bind=engine)

def getPlatforms():
    session = DBSession()
    allPlatforms = session.query(Platform).all()
    platformNameList = [p.platform for p in allPlatforms]
    session.close()
    return platformNameList

def create(platform_obj):
    session = DBSession()
    session.add(platform_obj)
    session.commit()

    return (f'{platform_obj.platform} successfully added!')

def read(platform_name):
    #takes an ID, returns an object from the database
    session = DBSession()
    result = session.query(Platform).filter(Platform.platform == platform_name).one()
    session.close()
    return result

def update(platformObj):
    #takes an object, updates object with values, returns success string
    session = DBSession()
    toUpdate = session.query(Platform).filter(Platform.platform == platformObj.platform).one()
    toUpdate.link = platformObj.link
    toUpdate.username = platformObj.username
    toUpdate.password = platformObj.password
    session.add(toUpdate)
    session.commit()
    session.close()
    return (f'{platformObj.platform} successfully updated!')

def delete(platform_name):
    session = DBSession()
    session.query(Platform).filter(Platform.platform == platform_name).delete()
    session.commit()
    session.close()
    return (f'{platform_name} has been successfully deleted!')