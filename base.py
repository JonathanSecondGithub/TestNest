from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('homepage.html', logged_in=True)


#new features

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/compiler')
def compiler():
    return render_template('compiler.html', langs=langs, logged_in=True)




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
