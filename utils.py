import sys


def clear_line():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
