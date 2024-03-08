#!/usr/bin/python3

import cmd
import shlex
from models.state import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB project.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Called when an empty line is entered.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): Any additional arguments passed.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.

        Args:
            arg (str): Any additional arguments passed.

        Returns:
            bool: True to exit the program.
        """
        print("Exiting the program...")
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it,

        Args:
            arg (str): The class name for which to create an instance.

        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance

        Args:
            arg (str): The class name and id of the instance.

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ['BaseModel', 'User', 'Place', 'City',
                              'State', 'Review', 'Amenity']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id

        Args:
            arg (str): The class name and id of the instance to be deleted.

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ['BaseModel', 'User','Place', 'City', 'State', 'Review', 'Amenity']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances

        Args:
            arg (str): The class name for which to print instances.

        """
        args = arg.split()
        if not args:
            print([str(obj) for obj in storage.all().values()])
            return

        class_name = args[0]
        if class_name not in ['BaseModel', 'User','Place', 'City', 'State', 'Review', 'Amenity']:
            print("** class doesn't exist **")
            return

        print([str(obj) for key, obj in storage.all().items() if key.startswith(class_name)])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by 

        Args:
            arg (str): The class name, id, attribute name, and attribute value.

        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ['BaseModel', 'User','Place', 'City', 'State',
                                'Review', 'Amenity']:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        instance = storage.all()[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def help_quit(self):
        """
        Help message for the quit command.
        """
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        """
        Help message for the EOF command.
        """
        print("Exit the program.")
        print()

    def help_create(self):
        """
        Help message for the create command.
        """
        print("Creates a new instance of BaseModel, saves it, and prints the id.")
        print("Usage: create <class_name>")
        print()

    def help_show(self):
        """
        Help message for the show command.
        """
        print("Prints the string representation of an instance based on class name and id.")
        print("Usage: show <class_name> <id>")
        print()

    def help_destroy(self):
        """
        Help message for the destroy command.
        """
        print("Deletes an instance based on class name and id.")
        print("Usage: destroy <class_name> <id>")
        print()

    def help_all(self):
        """
        Help message for the all command.
        """
        print("Prints all string representation of all instances based or not on the class name.")
        print("Usage: all [class_name]")
        print()

    def help_update(self):
        """
        Help message for the update command.
        """
        print("Updates an instance based on class name")
        print("Usage: update <class_name> <id> <attribute_name>")
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
