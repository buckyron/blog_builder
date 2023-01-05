import traceback
from model.postcomment import PostComment
# from model.posttag import PostTag
from util.service_result import ServiceResult
import pprint
from datetime import datetime
now = datetime.now()


def create_comment(comment, tag_id):
    result = ServiceResult()
    try:
        postComment = PostComment.insert_comment(comment=comment, tag_id=tag_id, comment_time=now)
        result.code = 201
        result.data = postComment
        return result.make_response()

    except:
        traceback.print_exc()
        result.code = 500
        return result.make_response()

def get_tag_comments(tag_id):
    result = ServiceResult()
    try:
        tag_comments = PostComment.get_tag_comments(tag_id=tag_id)
        result.data = tag_comments
        pprint.pprint(result.make_response())
        return result.make_response()
    except:
        traceback.print_exc()
        result.code = 500
        return result.make_response()
