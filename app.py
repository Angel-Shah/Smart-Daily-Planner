from flask import Flask, render_template, request, redirect
from config import Config
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from pytz import timezone
tz = timezone('EST')


app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)

class DailyTasks(db.Model):
    taskNumber = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.now(tz))

    def __repr__(self)-> str:
        return f"{self.taskNumber} - {self.title}"



@app.route('/', methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        if title and desc:    

            dailytasks = DailyTasks(title = title, desc = desc)
            db.session.add(dailytasks)
            db.session.commit()
        
    allTasks = DailyTasks.query.all()
        # print (allTasks)
        # return 'Hello, World!'
    return render_template('index.html', allTasks = allTasks)

@app.route('/finish')
def finish():
    allTasks = DailyTasks.query.all()
    print (allTasks)
    return 'Here are the products'

@app.route('/update/<int:taskNumber>',methods = ['GET','POST'])
def update(taskNumber):
    
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        task = DailyTasks.query.filter_by(taskNumber = taskNumber).first()
        task.title = title
        task.desc = desc
        db.session.add(task)
        db.session.commit()
        return redirect("/")

    taskToUpdate = DailyTasks.query.filter_by(taskNumber = taskNumber).first()
    return render_template('update.html', taskToUpdate = taskToUpdate)

@app.route('/delete/<int:taskNumber>')
def delete(taskNumber):
    taskToDelete = DailyTasks.query.filter_by(taskNumber = taskNumber).first()
    db.session.delete(taskToDelete)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True,port=1212)