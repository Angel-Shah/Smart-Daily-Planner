from flask import Flask, render_template, request, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
import pymongo 
from pymongo import MongoClient
from datetime import datetime
from pytz import timezone
tz = timezone('EST')

#mongodb+srv://Angel:dailytasks64@cluster0.a5gk4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

cluster = MongoClient("mongodb+srv://Angel:dailyTasksAppPass@cluster0.a5gk4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["DailyTasks-DB"]
collection = db["Tasks"]

collection.insert_one({ "title":"6th task", "desc":"6th task description here", "datetime": datetime.now(tz)})
