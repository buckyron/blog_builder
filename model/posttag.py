from config import db
from model.postcomment import PostComment
from sqlalchemy.orm import relationship


class PostTag(db.Model):
    __tablename__ = 'posttag'
    id          = db.Column('tag_id', db.Integer, primary_key = True)
    tag         = db.Column('tag', db.Text, nullable = False)
    tag_div_id  = db.Column('tag_div_id', db.String(16), nullable = False)
    post_id     = db.Column('post_id', db.Integer, db.ForeignKey('blogpost.post_id'))
    comments    = db.relationship('PostComment', backref="tag", cascade="all, delete")

    def json(self):
        return {
            "tag_id": self.id,
            "tag_div_id": self.tag_div_id,
            "tag"   : self.tag,
            "post_id": self.post_id
        }

    def get_post_tags(post_id):
        return [ PostTag.json(posttag) for posttag in PostTag.query.filter_by(post_id=post_id)]
