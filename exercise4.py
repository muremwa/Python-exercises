# You are writing a file browser which displays files line by line.
# The list of files is specified on the commands line (in sys.argv).
# After displaying one line, the program waits for user input.
# The user can:
#                 - press Enter to display the next line
#                 - press n + Enter to forget the rest of the current ﬁle and start with the next ﬁle
#                 - or anything else + Enter to display the next line
#
# The first part is already written:
# it is a function which displays the lines and queries the user for input.
# Your job is to write the second part — the generator read_lines with the following interface:
# during construction it is passed a list of files to read.
# If yields line after line from the first ﬁle, then from the second ﬁle, and so on.
# When the last ﬁle is exhausted, it stops.
# The user of the generator can also throw an exception into the generator (SkipThisFile) which
# signals the generator to skip the rest of the current ﬁle, and just yield a dummy value to be skipped.


class SkipThisFile(Exception):
    """Tells the generator to jump to the next file in list."""
    pass


def read_lines(*files):
    """this is the generator to be written"""
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                try:
                    yield line
                except SkipThisFile:
                    yield 'dummy'
                    break


def display_files(*files):
    source = read_lines(*files)
    for line in source:
        print(line, end='')
        inp = input()
        if inp == 'n':
            print('NEXT')
            source.throw(SkipThisFile)
            # return value is ignored


display_files('exercise1.py', 'exercise2.py', 'exercise3.py')
