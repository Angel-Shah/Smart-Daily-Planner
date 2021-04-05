from flask import Flask, render_template, request, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
import pymongo 
from pymongo import MongoClient
from datetime import datetime
from pytz import timezone
import json 
from bson import json_util
tz = timezone('EST')

#mongodb+srv://Angel:dailytasks64@cluster0.a5gk4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

cluster = MongoClient("mongodb+srv://Angel:dailyTasksAppPass@cluster0.a5gk4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["DailyTasks-DB"]
collection = db["Tasks"]

# collection.insert_one({"_id":0, "title":"task name", "desc":"random task desc"})

app = Flask(__name__)

app.config.from_object(Config)

# db = SQLAlchemy(app)

# class DailyTasks(db.Model):
#     taskNumber = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable = False)
#     desc = db.Column(db.String(500), nullable = False)
#     date_created = db.Column(db.DateTime, default = datetime.now(tz))

#     def __repr__(self)-> str:
#         return f"{self.taskNumber} - {self.title}"

taskId = 44

@app.route('/', methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if title and desc:    

            # dailytasks = DailyTasks(title = title, desc = desc)
            # db.session.add(dailytasks)
            # db.session.commit()
            collection.insert_one({"_id":taskId, "title":title, "desc":desc})
        
    allTasks = list(collection.find({}))
    # for task in allTasks:
    #     print(task)
    # print(allTasks[0]['title'])
    # print(len(allTasks))
    # return(json.dumps(allTasks,default=json_util.default))
        # print (allTasks)
        # return 'Hello, World!'
    return render_template('index.html', allTasks = allTasks)
    # return "homepage"

@app.route('/finish/<string:taskNumber>',methods = ['GET','POST'])
def finish(taskNumber):
    # allTasks = DailyTasks.query.all()
    # print (allTasks)
    return 'Here are the products'

@app.route('/update/<string:taskNumber>',methods = ['GET','POST'])
def update(taskNumber):
    # collection.insert_one({"_id":0, "title":"task name", "desc":"random task desc"})
    # if request.method == 'POST':
    #     title = request.form['title']
    #     desc = request.form['desc']
    #     task = DailyTasks.query.filter_by(taskNumber = taskNumber).first()
    #     task.title = title
    #     task.desc = desc
    #     db.session.add(task)
    #     db.session.commit()
    #     return redirect("/")

    # taskToUpdate = DailyTasks.query.filter_by(taskNumber = taskNumber).first()
    # return render_template('update.html', taskToUpdate = taskToUpdate)
    return "this is the update page"

@app.route('/delete/<string:taskNumber>')
def delete(taskNumber):
    # taskToDelete = DailyTasks.query.filter_by(taskNumber = taskNumber).first()
    # db.session.delete(taskToDelete)
    # db.session.commit()
    # return redirect("/")
    return "this is the delete function"

if __name__ == "__main__":
    app.run(port="1212")