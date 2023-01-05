from turtle import pos
from flask import jsonify, request, make_response
from service.posttag_services import get_post_tags


def getposttags(post_id):
    result = get_post_tags(post_id=post_id)
    return make_response(result)
