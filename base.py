from flask import Flask, render_template

app = Flask(__name__)


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


