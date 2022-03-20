from app import app 
from flask import render_template

@app.route('/')
def home():
    print('what up')
    return render_template('index.html')


@app.route('/characters')
def charcterslist():
    print('character list should go here')
    return render_template('character_list.html')