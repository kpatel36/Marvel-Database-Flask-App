from app import app 
from flask import render_template, request, url_for
from .forms import SearchForm

@app.route('/')
def home():
    print('what up')
    return render_template('homepage.html')


@app.route('/characters')
def characterslist():
    print('character list should go here')
    return render_template('character_list.html')

# @app.route('/search', methods=['GET','POST'])
# def char_search():
#     search_form=SearchForm()
#     if request.method =="POST":
#         print(search_form.characterName.data)
    
#     return render_template('character_search.html', search_form=search_form)