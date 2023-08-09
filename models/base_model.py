# import models
from uuid import uuid4
from datetime import datetime

class BaseModel:

    """this is the base for model for the airbnb"""

    def __init__(self, *arg, **kwargs):
        self.id = str(uuid.uuid4())
        self.created = datetime.now()
        self.updated = datetime.now()
        storage.new(self)

    def __str__(self):
        """returns the string official"""
        return
        