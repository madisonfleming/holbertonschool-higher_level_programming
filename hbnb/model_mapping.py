from app.extensions import db

#base model mapping - intranet example
from app import db
import uuid
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True  # This ensures SQLAlchemy does not create a table for BaseModel

    id = db.Column("id", db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = db.Column("created_at", db.DateTime, default=datetime.now())
    updated_at = db.Column("updated_at", db.DateTime, default=datetime.now(), onupdate=datetime.now())


#user model mapping 
from app.extensions import db, bcrypt
import uuid
from .base_model import BaseModel  # Import BaseModel from its module

class User(BaseModel):
    __tablename__ = 'users'

    first_name = db.Column("first_name", db.String(50), nullable=False)
    last_name = db.Column("last_name", db.String(50), nullable=False)
    email = db.Column("email", db.String(120), nullable=False, unique=True)
    password = db.Column("password", db.String(128), nullable=False)
    is_admin = db.Column("is_admin", db.Boolean, default=False)

    def hash_password(self, password):
        """Hash the password before storing it."""
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def verify_password(self, password):
        """Verify the hashed password."""
        return bcrypt.check_password_hash(self.password, password)


# String(120) for attributes where the length is not stated

#place model mapping
    #make sure you copy paste the imports into the model file
class Place(BaseModel):
    __tablename__ = 'places'

    id = db.Column("id", db.Integer, unqiue=True, primrary_key=True)
    title = db.Column("title", db.String(100), nullable=False)
    description = db.Column("title", db.String(120), nullable=True)
    price = db.Column("price", db.Float, nullable=False)
    latitude = db.Column("latitude", db.Float, nullable=False)
    longitude = db.Column("longitude", db.Float, nullable=False)

#review model mapping
class Review(BaseModel):
    __tablename__ = 'reviews'

    id = db.Column("id", db.Integer, unqiue=True, primrary_key=True)
    text = db.Column("text", db.String(120), nullable=False)
    rating = db.Column("rating", db.Integer, nullable=False)

#amenity model mapping
class Amenity(BaseModel): 
    __tablename__ = 'amenities'

    id = db.Column("id", db.Integer, unqiue=True, primrary_key=True)
    _name = db.Column("name", db.String(50), nullable=False)


# user repository from example

from app.models.user import User
from app import db
from app.persistence.repository import SQLAlchemyRepository

class UserRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(User)

    def get_user_by_email(self, email):
        return self.model.query.filter_by(email=email).first()


#review repository
class ReviewRepository(SQLAlchemyRepository):
    def __init__(self):
        super().__init__(Review)

    def get_review_by_place(self, place_id):
        return self.model.query.filter_by(place_id=place_id).first()
    

#update facade to refactor to use user and review repo and sqlalchemy repo
from app.services.repositories.user_repository import UserRepository

class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.review_repo = ReviewRepository()
        self.place_repo = SQLAlchemyRepository()
        self.amenity_repo = SQLAlchemyRepository()

    def create_user(self, user_data):
        user = User(**user_data)
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    def update_user(self, user_id, data):
        updated_user = self.user_repo.update(user_id, data)
        return updated_user


#relationships between entities using sqlalchemy

#backref: This creates a reverse relationship automatically. It adds a new property to the referenced table, 
#         allowing you to easily traverse the relationship from both sides.
#lazy: This determines when SQLAlchemy loads related data. Common options include:
#   select: Load related data when the parent object is accessed.
#   subquery: Load all related objects using a separate query when the parent object is accessed.
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db

#User and Place (one-to-many relationship)
class User(db.model):
    __tablename__ = 'users'
    places = relationship('Place', back_populates='user', lazy=True)

class Place(db.model):
    __tablename__ = 'places'
    user_id = Column(db.column, Integer, ForeignKey('user_id'), nullable=False)
    users = relationship('User', back_populates='place', lazy=True)


#Place and Review (one-to-many relationship)
class Place(db.model):
    __tablename__ = 'places'
    reviews = relationship('Review', backref='Place', lazy=True)

class Review(db.model):
    __tablename__ = 'reviews'
    place_id = Column(db.column, Integer, ForeignKey('place_id'), nullable=False)


#User and Review (one-to-many relationship)
class User(db.model):
    __tablename__ = 'users'
    reviews = relationship('Review', backref='user', lazy=True)

class Review(db.model):
    __tablename__ = 'reviews'
    user_id = Column(db.column, Integer, ForeignKey('user_id'), nullable=False)


#Place and Amenity (many-to-many relationship)
association_table = db.Table('association_table',
                             Column('places', Integer, ForeignKey('amenities', primary_key=True),
                                    Column('amenities', Integer, ForeignKey('places'), primary_key=True))
                                    )

class Place(db.model):
    __tablename__ = 'places'
    amenities = relationship('amenities', secondary=association_table, lazy='subquery', back_populates='places')

class Amenity(db.model):
    __tablename__ = 'amenities'
    id = Column(Integer, primary_key=True)
    places = relationship('places', secondary=association_table, lazy='subquery', back_populates='amenities')



#review relationships
   place_id = db.Column(db.String(100), db.ForeignKey('places.id'))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'))
    places = db.relationship('Place', back_populates='reviews', lazy=True)
    owner = db.relationship('User', back_populates='reviews', lazy=True)

#amenity relationships
# sqlalchemy relationship association table for Place and Amenity
#association_table = db.Table('association_table',
                            #db.Column('place_id', db.String(100), db.ForeignKey('places.id', primary_key=True),
                                #db.Column('amenity_id', db.String(100), db.ForeignKey('amenities.id'), primary_key=True))
                                #)

#class Amenity(BaseModel):
    # sqlalchemy model mapping for amenity
    #__tablename__ = 'amenities'
    #id = db.Column(db.String(100), primary_key=True)
    #_name = db.Column("name", db.String(50), nullable=False)

    # sqlalchemy relationship mapping for amenity
    #places = db.relationship('Place', secondary=association_table, lazy='subquery', back_populates='amenities')


#place relationships
 user_id = db.Column(db.String(100), db.ForeignKey('users.id'), nullable=False)
    owner = db.relationship('User', back_populates='places', lazy=True)
    reviews = db.relationship('Review', back_populates='places', lazy=True)
    #amenities = db.relationship('amenities', secondary=association_table, lazy='subquery', back_populates='places')
    
    
