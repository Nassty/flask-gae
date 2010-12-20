from google.appengine.ext import db

class User(db.Model):
    user = db.UserProperty()
    display_name = db.StringProperty()

class Thread(db.Model):
    author = db.ReferenceProperty(User)
    title = db.StringProperty()
    closed = db.BooleanProperty()
    def to_dict(self):
        return dict(author=self.author.nickname(),
                    title=self.title,
                    closed=self.closed, 
                    posts=[x.to_dict() for x in self.posts])

class Post(db.Model):
    author = db.ReferenceProperty(User)
    content = db.StringProperty(multiline=True)
    thread = db.ReferenceProperty(Thread, collection_name="posts")
    
    def to_dict(self):
        return dict(author=self.author,
                    content=self.content,
                    thread=self.thread.key())
