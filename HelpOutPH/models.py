from google.appengine.ext import db

class RescueReport(db.Model):
    names = db.StringProperty()
    location = db.StringProperty()
    situation = db.StringProperty()
    contactinfo = db.StringProperty()
    
class Tweet(db.Model):
    text = db.StringProperty()
    user = db.StringProperty