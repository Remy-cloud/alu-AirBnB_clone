#!/usr/bin/python3
"""
This module defines the command-line interpreter for the HBNB project.

It allows the user to interact with the program in a command-line environment
to create, retrieve, update, and delete instances of different models.
"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

# Dictionary to map model names to actual classes
MODELS = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "Amenity": Amenity,
}


def validate_args(args_list):
    """
    Validates command arguments to ensure they meet requirements.

    Args:
        args_list (list): The list of arguments passed by the user.

    Returns:
        bool: True if valid, False otherwise.
    """
    if not args_list:
        print("** class name missing **")
        return False

    class_name = args_list[0]
    if class_name not in MODELS:
        print("** class doesn't exist **")
        return False

    if len(args_list) < 2:
        print("** instance id missing **")
        return False

    return True


class HBNBCommand(cmd.Cmd):
    """Command interpreter for HBNB project"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles EOF (Ctrl+D) to exit the program"""
        print()
        return True

    def do_create(self, cls_name):
        """Creates an instance of a model"""
        if not cls_name:
            print("** class name missing **")
            return
        if cls_name not in MODELS:
            print("** class doesn't exist **")
            return

        new_model = MODELS[cls_name]()
        new_model.save()
        print(new_model.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        args_list = str.split(args)

        if not validate_args(args_list):
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance"""
        args_list = str.split(args)
        if not validate_args(args_list):
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        key = f"{class_name}.{instance_id}"
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, cls):
        """Prints all instances, or all instances of a specific class"""
        objects = storage.all()
        obj_list = []

        if not cls:
            for obj in objects.values():
                obj_list.append(str(obj))
        elif cls in MODELS:
            for key, obj in objects.items():
                if key.split(".")[0] == cls:
                    obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return

        print(obj_list)

    def do_update(self, args):
        """Updates an instance by adding or updating attributes"""
        args_list = args.split()

        if not validate_args(args_list):
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        if len(args_list) < 4:
            print("** value missing **")
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        attr_name = args_list[2]
        attr_value = args.split(" ", 3)[3]

        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]

        if attr_name in ["id", "created_at", "updated_at"]:
            return

        key = f"{class_name}.{instance_id}"
        objects = storage.all()

        if key in objects:
            instance = objects[key]
            try:
                if attr_value.isdigit():
                    attr_value = int(attr_value)
                else:
                    try:
                        attr_value = float(attr_value)
                    except ValueError:
                        pass
                setattr(instance, attr_name, attr_value)
                instance.save()
            except Exception as e:
                print(f"Error updating attribute: {e}")
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
