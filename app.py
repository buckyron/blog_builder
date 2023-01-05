from crypt import methods
from operator import imod
from flask import Flask  
from config import db
from api.blog_api import createblog,getblog, getblogposts
from api.blogpost_api import createblogpost, deleteblogpost, updateblogpost, getblogpost
from api.postcomment_api import create_comment, createcomment, gettagcomments
from api.posttag_api import getposttags
from flask_cors import cross_origin


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/demo'

db.init_app(app)

@app.route('/')
def main():
    return 'Hello, Typeset!'

# Blog start.
@app.route('/blog', methods = ['POST'])
@cross_origin()
def createBlog():
    return createblog()

@app.route('/blog/<int:blog_id>', methods = ['GET'])
@cross_origin()
def getBlog(blog_id):
    return getblog(blog_id)

@app.route('/blog/posts/<int:blog_id>', methods = ['GET'])
def getBlogPosts(blog_id):
    return getblogposts(blog_id)

# Blog ends.

# Blog Post starts.

@app.route('/blog/post', methods = ['POST'])
def createBlogPost():
    return createblogpost()

@app.route('/blog/post/<int:post_id>', methods=['GET'])
def getBlogPost(post_id):
    return getblogpost(post_id=post_id)

@app.route('/blog/post/<int:post_id>', methods = ['PUT'])
def editPost(post_id):
    return updateblogpost(post_id)

@app.route('/blog/post/<int:post_id>', methods = ['DELETE'])
def deletePost(post_id):
    return deleteblogpost(post_id=post_id)

# Blog Post ends.

# Blog comment starts.

@app.route('/blog/post/comment', methods = ['POST'])
def createComment():
    return createcomment()

@app.route('/blog/post/tag/<int:tag_id>/comment', methods = ['GET'])
def getTagComments(tag_id):
    return gettagcomments(tag_id=tag_id)

#Blog comment ends.

# Post tag starts

@app.route('/blog/post/<int:post_id>/tag', methods = ['GET'])
def getPostTags(post_id):
    return getposttags(post_id)

# Post tag ends



if __name__ == '__main__':
    app.run()
