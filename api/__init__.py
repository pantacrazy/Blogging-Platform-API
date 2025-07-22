from flask import Flask
import os
from .extensions import db
def create_app(test_config=None):
    app=Flask(__name__,instance_relative_config=True)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
    app.config.from_mapping(SECRET_Key='dev',SQLALCHEMY_DATABASE_URI=(
        'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db_name}'.format(
            user='root',      
            password='root', 
            host='localhost',           
            db_name='blog_db',
            port='3306'
        )
    ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False)
    
    if test_config is None:
        app.config.from_pyfile('config.py',silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    db.init_app(app)
    from . import blog
    app.register_blueprint(blog.bp)
    with app.app_context():
        db.create_all()
    return app