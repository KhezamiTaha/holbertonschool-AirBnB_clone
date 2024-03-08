#!/usr/bin/python3

import cmd
import json
from models.base_model import BaseModel
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
        Creates a new instance of BaseModel, saves it, and prints the id.

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

    def help_help(self):
        """
        Help message for the help command.
        """
        print("Show help information for commands.")
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()