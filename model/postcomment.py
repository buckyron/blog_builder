from sqlalchemy import false
from config import db

class PostComment(db.Model):
    __tablename__ = 'postcomment'
    id  = db.Column('comment_id', db.Integer, primary_key = True)
    comment     = db.Column('comment', db.Text, nullable = False)
    tag_id      = db.Column('tag_id', db.Integer, db.ForeignKey('posttag.tag_id'))
    comment_time= db.Column('comment_time', db.DateTime, nullable = False)

    def json(self):
        return {
            "comment_id": self.id,
            "comment"   : self.comment,
            "tag_id"    : self.tag_id,
            "comment_time": self.comment_time
        }

    
    def insert_comment(comment, tag_id, comment_time):
        post_comment = PostComment(comment=comment, tag_id=tag_id, comment_time=comment_time)
        db.session.add(post_comment)
        db.session.commit()
        return PostComment.json(post_comment)

    def update_comment(comment, comment_id, comment_time):
        postComment = PostComment.query.filter_by(id=comment_id).first()
        postComment.comment = comment
        postComment.comment_time = comment_time
        db.session.commit()
        return PostComment.json(postComment)

    def get_comment(comment_id):
        return PostComment.json(PostComment.query.filter_by(id=comment_id).first())
    
    def get_tag_comments(tag_id):
        return [PostComment.json(postcomment) for postcomment in PostComment.query.filter_by(tag_id=tag_id)]