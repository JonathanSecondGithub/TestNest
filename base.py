from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Teacher(db.Model):
    id = db.Column (db. Integer, primary_key=True)
    name = db.Column(db.String(50))
    tn = db.Column (db.String(100), unique=True)

@app.route('/')
def index():
        return render_template('index.html')

#routes for teachers
@app.route('/teacher')
def teacher():
            return render_template('teacher.html')

@app.route('/teacher/createtest')
def creattest():
                return render_template('creattest.html')

@app.route('/teacher/browse')
def teacherbrowse():
                return render_template('teacherbrowse.html')

#routes for students
@app.route('/student')
def student():
            return render_template('student.html')

@app.route('/student/test')
def studenttest():
            return render_template('studenttest.html')

@app.route('/teacher/questions')
def question():
                return render_template('question.html')
