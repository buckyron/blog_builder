import traceback
from model.blogpost import BlogPost
from util.service_result import ServiceResult
import pprint
from bs4 import BeautifulSoup
from datetime import datetime
now = datetime.now()


def create_blog_post(post_title, post_content, blog_id):
    print('serviice start')
    result = ServiceResult()
    try:
        soup = BeautifulSoup(post_content, 'html.parser')
        soup_tags = soup.find_all("div",{"class":"tag"})
        tags = list()
        for soup_tag in soup_tags:
            tag = {
                "tag_div_id": soup_tag.get('id'),
                "tag"       : soup_tag.getText()
            }
            tags.append(tag)

        post_description = soup.get_text()[:250]
        blogpost = BlogPost.insert_blog_post(post_title=post_title, post_description=post_description, post_content=post_content, posted_time=now, blog_id=blog_id, tags = tags)
        result.code = 201
        result.data = blogpost
        pprint.pprint(result)
        print('service success')
        return result.make_response()

    except:
        traceback.print_exc()
        result.code = 500
        return result.make_response()



def update_blog_post(post_id, post_title = None, post_content = None):
    result = ServiceResult()
    try:
        if post_content is None and post_title is None:
            result.code = 202
            return result.make_response()
        soup = BeautifulSoup(post_content, 'html.parser')
        soup_tags = soup.find_all("div",{"class":"tag"})
        tags = list()
        post_description = None
        if post_content is not None:
            for soup_tag in soup_tags:
                tag = {
                    "tag_div_id": soup_tag.get('id'),
                    "tag"       : soup_tag.getText()
                }
                tags.append(tag)
            post_description = soup.get_text()[:250]
        blogpost = BlogPost.update_blog_post(post_id=post_id, post_title=post_title, post_description=post_description, post_content=post_content, tags = tags)
        result.code = 202
        result.data = blogpost
        return result.make_response()

    except:
        traceback.print_exc()
        result.code = 500
        return result.make_response()


def get_blog_post(post_id):
    result = ServiceResult()
    try:
        blogPost = BlogPost.get_blog_post(post_id=post_id)
        result.data = blogPost
        pprint.pprint(result.make_response())
        return result.make_response()
    except:
        traceback.print_exc()
        result.code = 500
    return result.make_response()

def delete_blog_post(post_id):
    result = ServiceResult()
    try:
        blogPost = BlogPost.delete_blog_post(post_id=post_id)
        result.data = blogPost
        result.code = 204
        pprint.pprint(result.make_response())
        return result.make_response()
    except:
        traceback.print_exc()
        result.code = 500
    return result.make_response()

    