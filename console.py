#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
from shlex import split
from models import storage
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }

    def emptyline(self):
        """eliminate/ignore the empty spaces."""
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
            listy = line.split(" ")

            kwargs = {}
            for a in range(1, len(listy)):
                key, value = tuple(listy[a].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obc = eval(listy[0])()
            else:
                obc = eval(listy[0])(**kwargs)
                storage.new(obc)
            print(obc.id)
            obc.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        Exceptions:
            SyntaxError: when no args given
            NameError: when no object taht has the name
            IndexError: when no id given
            KeyError: when no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            listy = line.split(" ")
            if listy[0] not in self.__classes:
                raise NameError()
            if len(listy) < 2:
                raise IndexError()
            obx = storage.all()
            key = listy[0] + '.' + listy[1]
            if key in obx:
                print(obx[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        Exceptions:
            SyntaxError: when no args given
            NameError: when no object taht has the name
            IndexError: when no id given
            KeyError: when no valid id given
        """
        try:
            if not line:
                raise SyntaxError()
            my_listy = line.split(" ")
            if my_listy[0] not in self.__classes:
                raise NameError()
            if len(my_listy) < 2:
                raise IndexError()
            objec = storage.all()
            key = my_listy[0] + '.' + my_listy[1]
            if key in objec:
                del objec[key]
                storage.save()
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        if not line:
            a = storage.all()
            print([o[k].__str__() for q in a])
            return
        try:
            args = line.split(" ")
            if args[0] not in self.__classes:
                raise NameError()

            a = storage.all(eval(args[0]))
            print([o[k].__str__() for q in a])

        except NameError:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instanceby adding or updating attribute
        Exceptions:
            SyntaxError: when no args given
            NameError: when no object taht has the name
            IndexError: when no id given
            KeyError: when no valid id given
            AttributeError: when no attribute given
            ValueError: when no value given
        """
        try:
            if not line:
                raise SyntaxError()
            my_lists = split(line, " ")
            if my_lists[0] not in self.__classes:
                raise NameError()
            if len(my_lists) < 2:
                raise IndexError()
            objects = storage.all()
            key = my_lists[0] + '.' + my_lists[1]
            if key not in objects:
                raise KeyError()
            if len(my_lists) < 3:
                raise AttributeError()
            if len(my_lists) < 4:
                raise ValueError()
            num = objects[key]
            try:
                num.__dict__[my_lists[2]] = eval(my_lists[3])
            except Exception:
                num.__dict__[my_lists[2]] = my_lists[3]
                num.save()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def count(self, line):
        """count the number of instances of a class
        """
        counter = 0
        try:
            my_num = split(line, " ")
            if my_num[0] not in self.__classes:
                raise NameError()
            obj = storage.all()
            for key in obj:
                name = key.split('.')
                if name[0] == my_num[0]:
                    counter += 1
            print(counter)
        except NameError:
            print("** class doesn't exist **")

    def strip_clean(self, args):
        """strips the argument and return a string of command
        Args:
            args: input list of args
        Return:
            returns string of argumetns
        """
        num_list = []
        num_list.append(args[0])
        try:
            xdict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            xdict = None
        if isinstance(my_dict, dict):
            new_str = args[1][args[1].find('(')+1:args[1].find(')')]
            num_list.append(((new_str.split(", "))[0]).strip('"'))
            num_list.append(xdict)
            return new_list
        new_str = args[1][args[1].find('(')+1:args[1].find(')')]
        num_list.append(" ".join(new_str.split(", ")))
        return " ".join(a for a in num_list)

    def default(self, line):
        """retrieve all instances of a class and retrieve number of instances
        """
        mylist = line.split('.')
        if len(mylist) >= 2:
            if mylist[1] == "all()":
                self.do_all(mylist[0])
            elif mylist[1] == "count()":
                self.count(mylist[0])
            elif mylist[1][:4] == "show":
                self.do_show(self.strip_clean(mylist))
            elif mylist[1][:7] == "destroy":
                self.do_destroy(self.strip_clean(mylist))
            elif mylist[1][:6] == "update":
                args = self.strip_clean(mylist)
                if isinstance(args, list):
                    obq = storage.all()
                    key = args[0] + ' ' + args[1]
                    for k, v in args[2].items():
                        self.do_update(key + ' "{}" "{}"'.format(k, v))
                else:
                    self.do_update(args)
        else:
            cmd.Cmd.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
