import traceback
from model.blog import Blog
from model.posttag import PostTag
from util.service_result import ServiceResult
import pprint


def create_blog(blog_title):
    result = ServiceResult()
    try:
        blog = Blog.insert_blog(blog_title=blog_title)
        result.code = 201
        result.data = blog
        return result.make_response()

    except:
        traceback.print_exc()
        result.code = 500
        return result.make_response()

def get_blog(blog_id):
    result = ServiceResult()
    try:
        blog = Blog.get_blog(blog_id=blog_id)
        result.data = blog
        pprint.pprint(result.make_response())
        return result.make_response()
    except:
        traceback.print_exc()
        result.code = 500
        return result.make_response()

def get_blog_posts(blog_id, page, postsPerPage):
    result = ServiceResult()
    try:
        blog_posts = Blog.get_blog_posts(blog_id=blog_id, page=page, postsPerPage=postsPerPage)
        result.data = blog_posts
        pprint.pprint(result.make_response())
        return result.make_response()
    except:
        traceback.print_exc()
        result.code = 500
        return result.make_response()



