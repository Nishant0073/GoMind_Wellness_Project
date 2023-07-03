from flask import Flask, render_template, request, url_for , redirect
from pymongo import MongoClient

app = Flask(__name__)

# connection to database
client = MongoClient('localhost',27017, username="admin", password="Pass@123")

db = client.student_db
student_col = db.studentsData

if __name__ == '__main__':
    app.debug = True
    app.run()


# handling get and post request
@app.route('/', methods=('GET','POST'))
def index():
    if request.method=='POST':
        student_name = request.form['student_name']
        collage_name = request.form['collage_name']
        student_urn = request.form['student_urn']
        # saving data to to database
        student_col.insert_one({ 'student_name': student_name,'collage_name': collage_name,'student_urn': student_urn}),
        return redirect(url_for('index'))
    
    #fetch data from database
    all_students = student_col.find()
    return render_template('index.html', student_col=all_students) 

