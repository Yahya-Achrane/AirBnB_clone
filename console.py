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

    def do_create(self, arg):
        """
        Docs
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    obj = BaseModel()
                    obj.save()

                    print(obj.id)
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
