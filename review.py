import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the updated_at timestamp whenever the object is modified"""
        self.updated_at = datetime.now()

    def update(self, data):
        """Update the attributes of the object based on the provided dictionary"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.save()  # Update the updated_at timestamp

from base_model import BaseModel

class Review(BaseModel):
    """
    """
    def __init__(self, text, rating, place, user):
        super().__init__()

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

        self.validate() # Validate attribute values
        user.add_review(self) # Link review to User
        place.add_review(self) # Link review to Place

    def validate(self):
        if self.text is None or not isinstance(self.text, str):
            raise ValueError("content of review is required")

        if not isinstance(self.rating, int) or not (1 <= self.rating <= 5):
            raise ValueError("Rating must be within 1 to 5")

        if not self.place or not isinstance(self.place, Place): # must be a Place instance being reviewed
            raise ValueError("Place instance must exist")
                
        if not self.user or not isinstance(self.user, User): # must be a User instance leaving review
            raise ValueError("User instance must exist")
        
    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)
        review.user = self # Link back to user
        review.place = self # Link back to place
