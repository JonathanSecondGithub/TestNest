from flask import Flask, render_template, redirect, Response, jsonify
#from flask_sqlalchemy import SQLAlchemy

#database importations
'''
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, jwt_optional
from config import blacklist
from models.Post import Post
from config.lang_config import langs
from flask_mongoengine import MongoEngine
from models.User import User
from routes.api import api
from routes.user import user
from routes.post import post
import random


MAX_POSTS_GLOBAL_WALL = 100
MAX_POSTS_DASHBOARD = 100

db = MongoEngine()
'''


app = Flask(__name__)
'''
app.config['JWT_SECRET_KEY'] = '#OSTL@10@19@25@27#'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_COOKIE_CSRF_PROTECT'] = True


jwt = JWTManager(app)
db.init_app(app)

app.register_blueprint(api)
app.register_blueprint(user)
app.register_blueprint(post)
'''
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
        return render_template('compiler.html')

@app.route('/posts')
def posts():
            return render_template('poststest.html')

@app.route('/dashboard')
#@jwt_required
def dashboard():
    '''
    user = User.objects(username=get_jwt_identity())[0].to_mongo()
    posts = []
    for id in user['following']:
        u = User.objects(id=id)[0].to_mongo()
        for postid in u['posts']:
            if postid not in user['posts']:
                p = Post.objects(ID=postid)[0].to_mongo()
                p['by'] = u['username']
                posts.append(p)
    '''
    return render_template('dashboardtest.html')

@app.route('/challenge')
#@jwt_required
def challenge():
        return render_template('challengeform.html'/ ''', langs=langs''' ,logged_in=True)

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
