#!/usr/bin/python3
"""[summary]
"""

import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
import gc


class HBNBCommand(cmd.Cmd):
    """ cmd clone"""
    intro = 'Welcome to the Airbnb console. Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        """init method"""
        super().__init__(completekey, stdin, stdout)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit console"""
        return True

    def emptyline(self):
        """empty line. Do nothing"""
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """

        # TODO: make this common check a property
        if arg == "":
            print('** class name missing **')
            return
        try:
            model = models.classes[arg]()
            models.storage.new(model)
            models.storage.save()
            print(model.id)
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class `name` and `id`
        """
        if arg == "":
            print('** class name missing **')
            return

        try:
            model_name, model_id = arg.split(' ')
            model = models.storage.find(model_name, model_id)
            print(model.__str__())

        except Exception as e:

            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') > 1:
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if arg == "":
            print('** class name missing **')
            return

        try:
            model_name, model_id = arg.split(' ')
            models.classes[model_name]  # check the model is supported
            models.storage.delete(model_name, model_id)
            models.storage.save()

        except Exception as e:

            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') > 1:
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)
    def emptyline(self):
        """Define behaviour when an empty line is entered"""
        pass

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        if arg == "":
            print([x.__str__() for x in models.storage.all().values()])
        else:
            try:
                model = models.classes[arg]
                resp = []
                for l in models.storage.all().values():
                    if type(l) == model:
                        resp.append(l.__str__())
                print(resp)
            except Exception as e:
                print(e)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
    args = parse(arg)
        length_of_args = len(args)
        if length_of_args < 1:
            print("** class name missing **")
            return False
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return False
        elif length_of_args < 2:
            print("** instance id missing **")
            return False
        else:
            all_obj = models.storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key not in all_obj:
                print("** no instance found **")
                return False
            my_obj = all_obj[key]
        if length_of_args < 3:
            print("** attribute name missing **")
            return False
        elif length_of_args < 4:
            print("** value missing **")
            return False
        else:
            try:
                my_obj.__dict__["".join(args[2]).strip("\"\"")] = eval(args[3])
                my_obj.save()
            except NameError:
                my_obj.__dict__["".join(args[2]).strip("\"\"")] = args[3]
                my_obj.save()

    def do_count(self, arg):
        """
        Count all instances of a class
        Usage: "count" OR "count <class_name>"
        It can also be used to show all instances based on class name
        Example: count OR count BaseModel
        """

        args = parse(arg)
        all_obj = models.storage.all()
        if len(args) < 1:
            print(len(all_obj))
            return False
        if args[0] in classes:
            count = 0
            for i in all_obj.values():
                if i.__class__.__name__ == args[0]:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """ Method that handles unknown commands """

        args = tuple(line.split('.'))
        """if len(args) < 2 or args[0] not in classes:
            print("*** Unknown syntax:", line)
            return False"""
        if len(args) >= 2:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1][:4] == "show":
                self.do_show(stripper("show", args))
            elif args[1] == "count()":
                self.do_count(args[0])
            elif args[1][:7] == "destroy":
                self.do_destroy(args[0] + " " + args[1][8:-1].strip("\"\'"))
            elif args[1][:6] == "update":
                new_args = stripper("update", args)
                if isinstance(new_args, list):
                    obj = models.storage.all()
                    key = new_args[0] + ' ' + new_args[1]
                    for k, v in new_args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(new_args)
            else:
                print("*** Unknown syntax:", line)


classes = ("BaseModel", "User", "Place", "State", "City", "Amenity", "Review")


def parse(arg):
    """Convert input to a command and arguments"""

    return tuple(arg.split())


def stripper(method, args):
    """ Return clean string of arg """

    args = list(args)
    new_list = []
    new_list.append(args[0])
    if method == "show":
        new_list.append(str(args[1].strip("\")show(\"")))
    elif method == "update":
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
    return " ".join(i for i in new_list)


        if arg == "":
            print('** class name missing **')
            return

        try:
            # TODO: Handle case where the value to update has a space character
            model_name, model_id, attr, value = arg.split(' ')

            models.storage.update(model_name, model_id, attr, value)
            models.storage.save()

        except Exception as e:
            if arg.count(' ') == 0:
                print("** instance id missing **")
            elif arg.count(' ') == 1:
                print("** attribute name missing **")
            elif arg.count(' ') == 2:
                print("** value missing **")
            elif arg.count(' ') > 3:
                # TODO: Allow this case, and ignore the extra arguments
                print("** too many arguments (2 arguments required)**")
            else:
                print(e)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
