from fastapi import FastAPI

from sqlalchemy import  Column, Integer, String
from database import engine, Base 

class Userdata(Base):
    __tablename__ ="Userdata"

    id=Column(Integer,primary_key=True,index=True)
    Name=Column(String)
    Age=Column(Integer)
