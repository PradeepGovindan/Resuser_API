from sqlalchemy import Table, Column, Integer, Text, Float, ForeignKey, Date
from sqlalchemy.orm import mapper
from database import metadata, db_session

class BlogPost(object):
    query = db_session.query_property()
    def __init__(self, id=None, title=None, post=None):
        self.id = id
        self.title = title
        self.post = post

blog_posts = Table('blog_posts', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', Text),
    Column('post', Text)
)

mapper(BlogPost, blog_posts)


class Item_details(object):
    query = db_session.query_property()
    def __init__(self, item_id=None, item_name=None,carbon_intensity=None,type_name=None,kg=None):
        self.item_id = item_id
        self.item_name = item_name
        self.carbon_intensity=carbon_intensity
        self.type_name=type_name
        self.kg=kg

    def serialize(self):
     	return {"item_id":self.item_id,"item_name":self.item_name,"carbon_intensity":self.carbon_intensity,"type_name":self.type_name,"kg":self.kg}
        

items = Table('item_details', metadata,
    Column('item_id', Integer, primary_key=True),
    Column('item_name', Text),
    Column('type_name', Text),
    Column('carbon_intensity',Float),
    Column('kg',Float)
    
)

mapper(Item_details, items)


class Color(object):
    query = db_session.query_property()
    def __init__(self, color_id=None, color_name=None):
        self.color_id = color_id
        self.color_name = color_name

    def serialize(self):
     	return {"color_id":self.color_id,"color_name":self.color_name}
        

colors = Table('colors', metadata,
    Column('color_id', Integer, primary_key=True),
    Column('color_name', Text)
    
)

mapper(Color, colors)


class Year(object):
    query = db_session.query_property()
    def __init__(self, year_id=None, year_range=None):
        self.year_id = year_id
        self.year_range = year_range


    def serialize(self):
     	return {"year_id":self.year_id,"year_range":self.year_range}
        

years = Table('years', metadata,
    Column('year_id', Integer, primary_key=True),
    Column('year_range', Text)
    
)

mapper(Year, years)

class Postitem(object):
    query = db_session.query_property()
    def __init__(self, post_id=None,item_id=None,color_id=None,year_id=None,latitude=None,longitude=None,status=None):
        self.post_id=post_id
        self.item_id=item_id
        self.color_id=color_id
        self.year_id=year_id
        self.latitude=latitude
        self.longitude=longitude
        self.status=status

    def serialize(self):
     	return {"post_id":self.post_id,"item_id":self.item_id,"color_id":self.color_id,"year_id":self.year_id,"latitude":self.latitude,"longitude":self.longitude,"status":self.status}
        

posts = Table('posts', metadata,
    Column('post_id', Integer, primary_key=True),
    Column('item_id', Integer, ForeignKey(Item_details.item_id)),
    Column('color_id', Integer,ForeignKey(Color.color_id)),
    Column('year_id', Integer,ForeignKey(Year.year_id)),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('status', Integer),
    
)


mapper(Postitem, posts)

class Carbon(object):
    query = db_session.query_property()
    def __init__(self, record_id=None, item_name=None,carbon_intensity=None):
        self.record_id = record_id
        self.item_name = item_name
        self.carbon_intensity=carbon_intensity

    def serialize(self):
     	return {"record_id":self.record_id,"item_name":self.item_name,"carbon_intensity":self.carbon_intensity}
        

carbons = Table('carbonintensity', metadata,
    Column('record_id', Integer, primary_key=True),
    Column('item_name', Text),
    Column('carbon_intensity',Float)
    
)

mapper(Carbon, carbons)

class UserDetail(object):
	query = db_session.query_property()
	def __init__(self,user_email=None,user_name=None):
		self.user_email = user_email
		self.user_name = user_name
	def serialize(self):
		return {"user_email":self.user_email,"user_name":self.user_name}
        

userDetail = Table('user_details', metadata,
    Column('user_email', Text, primary_key=True),
    Column('user_name', Text)
    
    
)

mapper(UserDetail, userDetail)


class UserActivity(object):
    query = db_session.query_property()
    def __init__(self,record_id=None,user_email=None,post_id=None,contributed_date=None,activity_category=None):
    	self.record_id=record_id
    	self.user_email = user_email
    	self.contributed_date = contributed_date
    	self.post_id=post_id
    	self.activity_category=activity_category
        

    def serialize(self):
     	return {"record_id":self.record_id,"user_email":self.user_email,"post_id":self.post_id,"contributed_date":self.contributed_date,"activity_category":self.activity_category}
        

userActivity = Table('user_activity', metadata,
	Column('record_id', Integer, primary_key=True),
    Column('user_email', ForeignKey(UserDetail.user_email)),
    Column('post_id', Integer,ForeignKey(Postitem.post_id)),
    Column('contributed_date',Date),
    Column('activity_category',Integer)
    
    
)

mapper(UserActivity, userActivity)


