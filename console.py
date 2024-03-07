#!/usr/bin/python3
"""
The console : command line interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for HBNB project.

    Attributes:
        prompt (str): The command prompt string.
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

    def help_help(self):
        """
        Help message for the help command.
        """
        print("Show help information for commands.")
        print()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
