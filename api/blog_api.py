from pydoc import pager
from unittest import result
from flask import jsonify, request, make_response
from service.blog_services import create_blog, get_blog, get_blog_posts

def createblog():
    blog_json = request.get_json()
    result = create_blog(blog_json['blog_title'])
    return make_response(result)

def getblog(blog_id):
    result = get_blog(blog_id)
    return make_response(result)

def getblogposts(blog_id):
    page    = request.args.get('page')
    postsPerPage = request.args.get('postsPerPage')
    result = get_blog_posts(blog_id=blog_id, page=page, postsPerPage=postsPerPage)
    return make_response(result)