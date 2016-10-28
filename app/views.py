__author__ = 'Leo'
from app import app
from flask import render_template, flash, redirect
from app.forms import QuizForm, LoginForm
@app.route("/")
@app.route("/index")
@app.route("/questionform", methods = ['GET', 'POST'])
@app.route("/new")

@app.route('/login', methods = ['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('openid login="'+ form.openid.data + '", remember_me='+str(form.remember_me.data))
#         return redirect('/index')
#     return render_template('login.html',
#         title = 'Sign In',
#         form = form)

def questionform():
    pictures = [
        {'number':1, 'href':"http://img0.liveinternet.ru/images/attach/d/1/132/163/132163790_0ntoPM4Zqns.jpg"},
        {'number':2, 'href':"http://img0.liveinternet.ru/images/attach/d/1/132/163/132163810_wZYrWxdUpSU.jpg"},
        {'number':3, 'href': "http://img0.liveinternet.ru/images/attach/d/1/132/163/132163890_hsIiuImvA68.jpg"}
    ]
    form = QuizForm()
    return render_template("questionform.html",
                           title = "Quiz",
                           pictures = pictures,
                           form = form)

def index():
    user = {'nickname': 'Leo Zisser'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'there is no God but Allah and Muhammad is his Prophet'
        },
        {
            'author': {'nickname': 'Bill'},
            'body': 'Hail Satan, pals!'
        }

    ]
    return render_template("index.html",
                           title="home",
                           user=user,
                           posts=posts
                           )
