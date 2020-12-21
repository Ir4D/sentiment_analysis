from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_text = db.Column(db.Text, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    num_likes = db.Column(db.Integer, nullable=False)
    num_comments = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<post {} {}>'.format(self.title, self.url)