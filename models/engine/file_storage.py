import json
import os
# sys.path.append('../models')
# from models.base_model import BaseModel
# from models import Base_Model
# from models.user import User
# from models.state import State
# from models.city import City
# from models.place import Place
# from models.amenity import Amenity
# from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj.id}"
        FileStorage.__objects[key] = obj 

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        obj_dict = FileStorage.__objects
        d = {k:v.to_dict for k, v in obj_dict.items()}
        with open(FileStorage.__file_path, 'a') as f:
            json.dump(d, f)
    

    
    
    def reload(self):
        # """Deserialize the JSON file __file_path to __objects, if it exists."""
        file = FileStorage.__file_path
        # try:
            # with open(file, 'r',) as f:
                # obj_dict = json.load(f)
                # for k, v in obj_dict.items():
                    # obj_dict = {k: self.classes()[v["__class__"]](**v)}
                    # cls_name = o["__class__"]
                    # print(cls_name)
                    # del o["__class__"]
                    # self.new(eval(cls_name)(**o))
                    # print( self.classes()[v["__class__"]](**v))
                # FileStorage.__objects = obj_dict
        # except FileNotFoundError:
            # return
    def reload(self):
        """Reloads the stored objects"""
        try:
            with open(FileStorage.__file_path, "r",     encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v ["__class__"]](**v)for k, v in   obj_dict.items()}
                FileStorage.__objects = obj_dict
        except FileNotFoundError:
            return




    def classes(self):
        # """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes


    def attributes(self):
            """Returns the valid attributes and     their types for classname"""
            attributes = {
                "BaseModel":
                         {"id": str,
                          "created_at": datetime.   datetime,
                          "updated_at": datetime.   datetime},
                "User":
                         {"email": str,
                          "password": str,
                          "first_name": str,
                          "last_name": str},
                "State":
                         {"name": str},
                "City":
                         {"state_id": str,
                          "name": str},
                "Amenity":
                         {"name": str},
                "Place":
                         {"city_id": str,
                          "user_id": str,
                          "name": str,
                          "description": str,
                          "number_rooms": int,
                          "number_bathrooms": int,
                          "max_guest": int,
                          "price_by_night": int,
                          "latitude": float,
                          "longitude": float,
                        "amenity_ids": list},
                        "Review":
                        {"place_id": str,
                             "user_id": str,
                             "text": str}
            }
            return attributes

b= FileStorage()



