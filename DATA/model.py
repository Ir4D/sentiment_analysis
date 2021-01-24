from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, primary_key=True)
    #group_url = db.Column(db.String, unique=True, nullable=False) #добавил на случай, если будем работать с разными группами, а не только с одной
    post_likes_count = db.Column(db.Integer, nullable=False)
    post_comments_count = db.Column(db.Integer, nullable=False)
    post_published = db.Column(db.DateTime, nullable=False)
    post_text = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def __repr__(self):
        return '<Post {} {}>'.format(self.post_id, self.post_likes_count)


class Comment(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.post_id', ondelete='CASCADE'), index=True)
    comment_likes_count = db.Column(db.Integer, nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post', backref='comment')

    def __repr__(self):
        return '<Comment {} {}>'.format(self.comment_id, self.comment_text)

