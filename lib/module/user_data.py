from google.appengine.ext import db

class PersonalData(db.Model):
  user_id = db.IntegerProperty()
  name    = db.StringProperty()
  gender  = db.IntegerProperty()
  avatar  = db.StringProperty()