


from flask import  Flask
from flask_migrate import Migrate
from post.models import  db
from post.config import  projectConfig as AppConfig  
from post.models import Post
from flask import  render_template
from post.post_crud.api.api_views import AllPosts,PostGetSpecificAndUpdateAndDelete

from flask_restful import Api

def create_app(config_name):
    app = Flask(__name__)
    current_config = AppConfig[config_name]  # class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config # search in this class about class variable with this name
    app.config['SECRET_KEY'] = current_config.SECRET_KEY
    app.config.from_object(current_config)
    db.init_app(app)

    migrate = Migrate(app, db, render_as_batch=True)


    from post.post_crud import post_blueprint
    app.register_blueprint(post_blueprint)

    api = Api(app)
    api.add_resource(AllPosts, '/api/posts')
    api.add_resource(PostGetSpecificAndUpdateAndDelete, '/api/posts/<int:id>')



    return  app