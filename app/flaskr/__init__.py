import os
import requests
import json

from flask import Flask, render_template, request


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/', methods=('GET', 'POST'))
    def getPost():
        if request.method == 'POST':
            title = request.form['title']
            data = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={title}&number=100&apiKey=8f76aac47cef4f23874744431bd6424a").json()
            print(request.headers)
            return render_template('test.html',data=data)
        else:
            return render_template('index.html')
    
    @app.route('/recipeinfo/<id>')
    def getId(id):
        data = requests.get(f'https://api.spoonacular.com/recipes/{id}/information?includeNutrition=false&apiKey=8f76aac47cef4f23874744431bd6424a').json()
        return data
    return app