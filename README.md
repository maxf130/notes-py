# notes-py - Yet another static site generator.

notes-py is a _dumb_ static site generator.  Fundamentally it uses [rtfd/CommonMark-py](https://github.com/rtfd/CommonMark-py) to compile html from markdown files (like basically every other static site generator).

## Installation

Since notes-py is self contained (within notes-py/notes.py), you can just download and install this file somewhere in your path to use it.  I will make it available on PyPi shortly, so you should be able to install it with `pip install notes-py` as well.

If installed with pip, it will also install an entry point at compile_notes, which behaves effectively as a link to notes_py.notes.

## Usage
notes-py offers both a command line and programmatic interface.
### Command line
To keep the command line options simple, the only thing you need to specify is the location of a configuration file:
```
usage: compile_notes [-c path_to_config] [options]

Options:
    -h, --help    : Print this help text
    -c, --config  : Specipy the path to a configuration file
    -V, --version : Print version and licence info
```
### Programmatic
The full functionalitly (it isn't much) is available through the function at `notes_py.notes.compile(content_path, compile_path, stylesheet, html_template)`.  If you are using notes-py programmatically then you should just read through the function to understand whatit does. 

## Contact
You can reach me at max@friedersdorff.com
