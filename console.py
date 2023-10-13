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

    def do_show(self, arg):
        """
        show docs goes here
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "BaseModel.{}".format(args_array[1])
                        if search_string in objs_dict:
                            print(objs_dict[search_string])
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Destroy docs goes here
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "BaseModel.{}".format(args_array[1])
                        if search_string in objs_dict:
                            del(objs_dict[search_string])
                            models.storage.save()
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        empty for now
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    final_list = []
                    for key, value in models.storage.all().items():
                        if ("BaseModel" in key):
                            final_list.append(str(value))
                    print(final_list)
                else:
                    print("** class doesn't exist **")
        else:
            final_list = []
            for key, value in models.storage.all().items():
                final_list.append(str(value))
            print(final_list)

    def do_update(self, arg):
        """
        update docs ..
        """
        if len(arg) > 0:
            args_array = arg.split()
            if len(args_array) > 0:
                if args_array[0] == "BaseModel":
                    if len(args_array) > 1:
                        objs_dict = models.storage.all()
                        search_string = "BaseModel.{}".format(args_array[1])
                        if search_string in objs_dict:
                            if len(args_array) > 2:
                                if len(args_array) > 3:
                                    if (args_array[3] not in ["created_at", "updated_at", "id"]):
                                        setattr(objs_dict[search_string], str(args_array[2]), str(args_array[3]))
                                else:
                                    print("** value missing **")
                            else:
                                print("** attribute name missing **")
                        else:
                            print("** no instance found **")
                    else:
                        print("** instance id missing **")
                else:
                    print("** class doesn't exist **")
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
