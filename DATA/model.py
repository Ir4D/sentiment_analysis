from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class post(db.Model):
    group_url = db.Column(db.String, unique=True, nullable=False) #добавил на случай, если будем работать с разными группами, а не только с одной
    id = db.Column(db.Integer, primary_key=True)
    post_text = db.Column(db.Text, nullable=False)
    post_published = db.Column(db.DateTime, nullable=False)
    num_post_likes = db.Column(db.Integer, nullable=False)
    num_post_comments = db.Column(db.Integer, nullable=False)
    comment_text = db.Column(db.Text, nullable=False)
    num_comm_likes = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<post {} {}>'.format(self.title, self.url)