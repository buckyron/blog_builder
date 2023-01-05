from flask import jsonify, request, make_response
from service.blogpost_services import create_blog_post, delete_blog_post, get_blog_post, update_blog_post
import pprint

def createblogpost():
    blogpost_json   = request.get_json()
    post_title      = blogpost_json['post_title']
    post_content    = blogpost_json['post_content']
    blog_id         = blogpost_json['blog_id']
    result = create_blog_post(post_title=post_title, post_content=post_content, blog_id=blog_id)
    return make_response(result)

def updateblogpost(post_id):
    blogpost_json   = request.get_json()
    post_title      = blogpost_json['post_title'] if 'post_title' in blogpost_json else None
    post_content    = blogpost_json['post_content'] if 'post_content' in blogpost_json else None
    result = update_blog_post(post_title=post_title, post_content=post_content, post_id=post_id)
    return make_response(result)

def getblogpost(post_id):
    result = get_blog_post(post_id=post_id)
    return make_response(result)

def deleteblogpost(post_id):
    result = delete_blog_post(post_id=post_id)
    return make_response(result)
