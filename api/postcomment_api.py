from flask import jsonify, request, make_response
from service.post_comment_services import create_comment, get_tag_comments

def createcomment():
    blog_json   = request.get_json()
    comment     = blog_json['comment']
    tag_id      = blog_json['tag_id']
    result = create_comment(comment=comment, tag_id=tag_id)
    return make_response(result)

def gettagcomments(tag_id):
    result = get_tag_comments(tag_id=tag_id)
    return make_response(result)