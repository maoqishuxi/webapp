from flask import render_template, flash, redirect, url_for

from app import app
from app.form import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, password: {}, remember_me={}'.format(
            form.username.data, form.password.data, form.remember_me.data
        ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sigin In', form=form)

@app.route('/video')
def video():
    with open("E:/work/python/usually/webapp/static/vedio", 'r', encoding='utf-8') as f:
        data = []
        for i in f:
            if i[0] != 'h':
                text = i.replace('    ', '').split(' ')
                print(text[len(text) - 2:])
                data.append(text[len(text) - 2:])
            else:
                print(i)
                data.append(i)
    return render_template('video.html', vedio=data)
