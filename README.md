# humanize-gcode

A tool for explaining the commands in machine readable GCode files.

Based on the specified GCode flavour, the tool parses a list of GCode commands and their description from the flavour's documentation. With this library it parses the input file and explains the effect of each command.

#### Installation

The utility is available on PyPi, so it can be installed with `pip`:

`pip3 install humanize-gcode`

#### Usage

The package comes with the executable script `hucode` that accepts two arguments. The GCode flavour (currently only `marlin/smoothie` are supported) and the name of the file to annotate (or `-` for stdin).

##### Example usage

`~ hucode smoothie testfile.gcode`

![Example output](https://i.imgur.com/u87tTqs.png)

#### TODO

- More output formats (and possibly customization?)
- More supported GCode flavours
- Use command arguments to influence annotation
- Caching of GCode flavour libraries

