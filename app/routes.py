from app import app
from flask import render_template, request
from app.forms import UserInfoForm, PostForm
@app.route('/')
@app.route('/index')
def hello_world():
    context = {
        'title': 'Austin Phonebook | HOME'        
    }
    return render_template('index.html', **context)


@app.route('/register_phone_number', methods=['GET', 'POST'])
def register_phone_number():
    title = "Austin Phonebook | REGISTER"
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        password = form.password.data
        print(first_name, last_name, phone, password)
    return render_template('register_phone_number.html' , title=title, form=form)



@app.route('/post_comment', methods=['GET', 'POST'])
def post_comment():
    title = "Austin Phonebook | COMMENT"
    post = PostForm()
    if request.method == 'POST' and post.validate():
        post_title = post.title.data
        content = post.content.data
        print(post_title, content)
    return render_template('post_comment.html', post=post, title=title)