import sqlite3, os, math, sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#declare the class
Base = declarative_base()
class Platform(Base):
    __tablename__ = 'logInData'
    platform = Column(String(250), primary_key = True)
    link = Column(String(250), nullable=True)
    username = Column(String(250), nullable=True)
    password = Column(String(250), nullable=True)

#check if database exists, if not, create one with the right table

#set up the session factory
engine = create_engine('sqlite:///passwordManager.db')
DBSession = sessionmaker(bind=engine)

def getPlatforms():
    session = DBSession()
    allPlatforms = session.query(Platform).all()
    platformNameList = [p.platform for p in allPlatforms]
    print(platformNameList)
    session.close()
    return platformNameList

def create(platform_obj):
    session = DBSession()
    session.add(platform_obj)
    session.commit()
    session.close()
    return "you son of a bitch, I'm in"

def read(platform_name):
    #takes an ID, returns an object from the database
    session = DBSession()
    result = session.query(Platform).filter(Platform.platform == platform_name).one()
    session.close()
    return result

def update(platformObj):
    #takes an object, updates object with values
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
    return True