from flask_restful import Resource, Api, marshal_with, abort
from post.models import Post
from post.post_crud.api.serilizers import postserilizer,CategorySerilizer
from  post.post_crud.api.parser import  postparser
from post.models import db


class AllPosts(Resource):
    @marshal_with(postserilizer)
    def get(self):
        posts=  Post.query.all()
        return posts

    @marshal_with(postserilizer)
    def post(self):
        posts = postparser.parse_args() 
        post = Post(**posts)
        db.session.add(post)
        db.session.commit()
        return  post, 201
    
class PostGetSpecificAndUpdateAndDelete(Resource):
    @marshal_with(postserilizer)
    def get(self, id):
        post = Post.query.get(id)
        if post:
            return post, 200

        return abort(404, message="Post not found Please Enter Your valid Id.")

    @marshal_with(postserilizer)
    def put(self, id):
        post = Post.query.get(id)
        if post:
            post_args = postparser.parse_args()
            post.update_post(post_args)
            return post, 200

        return abort(205, message="Post not found Please Enter Your valid Id.")

    def delete(self, id):
        post = Post.query.get(id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return {"This Post":"Deleted Successfully."}
        return abort(205,'Post not found , please reload the page')
    
    
    
    
    
    
    