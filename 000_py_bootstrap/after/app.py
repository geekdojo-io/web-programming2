#from flask import Flask # 1
from flask import Flask, render_template # 2 (p.26)
from flask_bootstrap import Bootstrap #3
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# from .forms import NameForm

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret'
bootstrap = Bootstrap(app)

# # 1
# @app.route('/')
# def home():
#     return '<h1>Hello World!</h1>'

# # 1
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!'.format(name)

# 2 (p.26)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    form = NameForm()

    return render_template('contact.html', form=form)

# 2 (p.26)
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)




