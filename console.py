#!/usr/bin/python3
"""
Defines the HBNB console.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        quit
        """
        return True

    def do_EOF(self, args):
        """
        eof
        """
        return True

    def emptyline(self):
        """
        empty
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
