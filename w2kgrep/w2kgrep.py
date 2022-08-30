import os
import sys
import glob


def command_filter(args):
    filtered = []
    for (i, arg) in enumerate(args):
        if arg in ["energy", "ENE", "ene", "EN", "en", "E", "e", ":ENE"]:
            filtered.append(":ENE")
        elif arg in ["fermi", "eF", "FER", "EF", "ef", ":FER"]:
            filtered.append(":FER")
        elif arg in [":MMI", "MMI", "mm", "mom", "MOM", "MM", "magmoment", "moment"]:
            try:
                atom = int(args[i + 1])
                atom = "00" + str(atom) if atom < 10 else "0" + str(atom)
                filtered.append(":MMI" + atom)
            except Exception:
                filtered.append(":MMI")
        else:
            filtered.append(arg)
    return filtered


class GREP(object):
    def __init__(self, filename=None, *args):
        self.filename = filename if filename is not None else glob.glob(
            "*scf")[0]
        self.keywords = [arg for arg in args if "-" not in arg[0]]
        self.options = [arg for arg in args if "-" in arg[0]]
        self.searches = command_filter(self.keywords)

    def grep(self):
        f = open(self.filename)
        lines = f.readlines()
        f.close()
        for search in self.searches:
            new_grep = [line for line in lines if search in line]
            if "-last" in self.options or "--last" in self.options:
                print(new_grep[-1], end="")
            elif "-first" in self.options or "--first" in self.options:
                print(new_grep[0], end="")
            else:
                for find in new_grep:
                    print(find, end="")


def main():
    orig_command_line = sys.argv[1:]
    filename = orig_command_line[-1] if "." in orig_command_line[-1] else None
    command_line = orig_command_line[:-
                                     1] if filename is not None else orig_command_line
    grep_cli = GREP(filename, *command_line)
    grep_cli.grep()
