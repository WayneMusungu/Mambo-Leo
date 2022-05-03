from flask import render_template
from app import app
from .request import get_category, get_source,article_source


#our views
@app.route('/')
def index():
    '''
    Root function returning home page with data
    '''
    source= get_source()
    print(source)
    return render_template('index.html',sources=source)

@app.route('/article/<id>')
def article(id):
    '''
    view article page function that returns article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html',articles= articles,id=id)


@app.route('/categories/<cat_name>')
def categories(cat_name):

    '''
    View categories that return articles relevant to the category
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name
    return render_template('categories.html',title = title,category=category, cat= cat_name)

