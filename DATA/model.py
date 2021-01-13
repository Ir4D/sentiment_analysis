from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_url = db.Column(db.String, unique=True, nullable=False) #добавил на случай, если будем работать с разными группами, а не только с одной
    post_id = db.Column(db.Integer, nullable=False)
    post_text = db.Column(db.Text, nullable=False)
    post_published = db.Column(db.DateTime, nullable=False)
    num_post_likes = db.Column(db.Integer, nullable=False)
    num_post_comments = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Post {} {}>'.format(self.post_id, self.num_post_likes)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    comment_id = db.Column(db.Integer, nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    num_comment_likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Comment {} {}>'.format(self.comment_id, self.num_comment_likes)
