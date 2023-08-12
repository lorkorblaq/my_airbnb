import json
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
    __objects = {'key':'value' }

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        obj_type_name = type(obj)
        obj_id=obj.id
        # key = "{}.{}".format(type(obj).__name__, obj.id)
        # FileStorage.__objects[key] = obj 
        print(obj_type_name,obj_id)

    def save(self):
        obj_dict = FileStorage.__objects
        with open(FileStorage.__file_path, 'a') as f:
            d = {k:v for k, v in obj_dict.items()}
            json.dump(d, f)
            #print(k)
                # d= d.to_dict()
    def reload(self):
        file = FileStorage.__file_path
        try:
            with open(file, 'r') as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
    
    
    
        

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
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
                
        

    
    

    
    
    

b=FileStorage()
print(b.all())
print(b.new('5'))