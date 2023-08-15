
"""Defines the BaseModel class."""
# from models import *
import sys
sys.path.append("my_airbnb")
# from engine.file_storage import save
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is the BaseModel of the HBnB project by alx."""

    def __init__(self, *args, **kwargs):
        """This Initialize this BaseModel.
        Arguments:
            *arguments args (any): Unused.
            **keyword arguments kwargs (dict): Key/value pairs of attributes.
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.name = 'femi'
        self.my_number = 0
        self.created_at = datetime.today().isoformat()
        self.updated_at = datetime.today().isoformat()
        if len(kwargs) != 0:
            for k,v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] =datetime.strtime(v,timeform)
            
        # print(self.id)
    def __str__(self):
        class_name = self.__class__.__name__
        return f"This class_name is {class_name}, \nIts id: {self.id}, and it conatins these:\n {self.__dict__}"

    #def save():
     #   pass


    def to_dict():
        diction = self.__dict__
        pass

        # if len(kwargs) != 0:
            # for k, v in kwargs.items():
                # if k == "created_at" or k == "updated_at":
                    # self.__dict__[k] = datetime.strptime(v, tform)
                    # print(self.__dict__[k])
                # else:
                    # self.__dict__[k] = v
        # else:
            # pass
            # models.storage.new(self)
b = BaseModel()
b.name = "Perpe"
b.my_number = 89
print(b)







    # def save(self):
        # """Update updated_at with the current datetime."""
        # self.updated_at = datetime.today()
        # models.storage.save()

    # def to_dict(self):
        # """Return the dictionary of the BaseModel instance.
        # Includes the key/value pair __class__ representing
        # the class name of the object.
        # """
        # rdict = self.__dict__.copy()
        # rdict["created_at"] = self.created_at.isoformat()
        # rdict["updated_at"] = self.updated_at.isoformat()
        # rdict["__class__"] = self.__class__.__name__
        # return rdict

    # def __str__(self):
        # """Return the print/str representation of the BaseModel instance."""
        # clname = self.__class__.__name__
        # return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
