"""PyTG

Usage:
    pytg (<command>) [options] [<parameter>...]

--source-only       Act on source files only (maintain content folder of a given module)
"""
import importlib

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.1')

    command = arguments["<command>"]

    importlib.import_module(f"pytg.commands.{command}").exec()
