import traceback
from model.posttag import PostTag
from util.service_result import ServiceResult
import pprint

def get_post_tags(post_id):
    result = ServiceResult()
    try:
        postTags = PostTag.get_post_tags(post_id=post_id)
        result.data = postTags
        pprint.pprint(result.make_response())
        return result.make_response()
    except:
        traceback.print_exc()
        result.code = 500
        return result.make_response()

        