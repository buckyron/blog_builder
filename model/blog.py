from turtle import end_fill
from config import db
from sqlalchemy.orm import relationship

from model.blogpost import BlogPost


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column('blog_id', db.Integer, primary_key = True)
    blog_title = db.Column('blog_title', db.String(50), nullable = False)
    blog_posts = relationship('BlogPost', backref= 'blog', cascade="all, delete")

    def json(self):
        return {
            'blog_id': self.id,
            'blog_title': self.blog_title
        }

    def insert_blog(blog_title):
        blog = Blog(blog_title=blog_title)
        db.session.add(blog)
        db.session.commit()
        return Blog.json(blog)

    def get_blog(blog_id):
        return Blog.json(Blog.query.filter_by(id=blog_id).first())

    def get_blog_posts(blog_id, page, postsPerPage):
        paginated_posts = BlogPost.query.filter_by(blog_id=blog_id).paginate(int(page), int(postsPerPage), False)
        hasNext         = paginated_posts.has_next
        blogposts = paginated_posts.items
        blogposts_json = [ BlogPost.json(blogpost) for blogpost in blogposts]
        blogposts_data  = {
            "posts": blogposts_json,
            "hasNext": hasNext
        }
        return blogposts_data