from pprint import pprint
from sqlalchemy.orm import relationship
from config import db
from model.posttag import PostTag


class BlogPost(db.Model):
    __tablename__ = 'blogpost'
    id                  = db.Column('post_id', db.Integer, primary_key = True)
    post_title          = db.Column('post_title', db.String(50), nullable = False)
    post_description    = db.Column('post_description', db.Text, nullable = False)
    post_content        = db.Column('post_content', db.Text, nullable = False)
    blog_id             = db.Column('blog_id', db.Integer, db.ForeignKey('blog.blog_id'))
    posted_time         = db.Column('posted_time', db.DateTime, nullable = False)
    tags                = db.relationship('PostTag', backref='post', cascade="all, delete")

    def json(self):
        return {
            "post_id": self.id,
            "post_title": self.post_title,
            "post_description": self.post_description,
            "post_file": self.post_content,
            "blog_id": self.blog_id,
            "posted_time": self.posted_time
        }

    def insert_blog_post(post_title, post_description, post_content, blog_id, posted_time, tags):
        blogpost = BlogPost(post_title=post_title, post_description=post_description, post_content=post_content, blog_id=blog_id, posted_time=posted_time)
        db.session.add(blogpost)
        print(blogpost)
        if len(tags) > 0:
            for tag in tags:
                posttag = PostTag(tag=tag['tag'], tag_div_id=tag['tag_div_id'], post = blogpost)

                db.session.add(posttag)
        db.session.commit()
        return BlogPost.json(blogpost)

    def update_blog_post(post_id, post_title = None, post_description = None, post_content = None, tags = None):
        blogPost = BlogPost.query.filter_by(id=post_id).first()
        blogPost.post_title = post_title if post_title != blogPost.post_title and post_title is not None else blogPost.post_title 
        blogPost.post_description = post_description if post_description  != blogPost.post_description and post_description is not None else blogPost.post_description
        blogPost.post_content = post_content if post_content  != blogPost.post_content and post_content is not None else blogPost.post_content
        posttags_div_ids = []
        for bp_tag in blogPost.tags:
            posttags_div_ids.append(bp_tag.tag_div_id)
        if len(tags) > 0:
            for tag in tags:
                pprint(tag['tag'])
                if tag['tag_div_id'] in posttags_div_ids:
                    posttag = PostTag.query.filter_by(tag_div_id=tag['tag_div_id']).first()
                    if posttag != tag['tag']:
                        posttag.tag = tag['tag']
                    
                else:
                    posttag = PostTag(tag=tag['tag'], tag_div_id=tag['tag_div_id'], post = blogPost)
                    db.session.add(posttag)

        db.session.commit()
        return BlogPost.json(blogPost)

    def get_blog_post(post_id):
        blogpost    = BlogPost.query.filter_by(id=post_id).first()
        tags        = blogpost.tags
        blogpost_json = BlogPost.json(blogpost)
        tags_json        = [PostTag.json(tag) for tag in tags]
        blogpost_data = {
            "post": blogpost_json,
            "tags": tags_json
        }
        return blogpost_data
    
    def delete_blog_post(post_id):
        blogPost = BlogPost.query.filter_by(id=post_id).first()
        db.session.delete(blogPost)
        db.session.commit()
        return BlogPost.json(blogPost)