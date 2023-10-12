# Organise4M
Organisation tools for Maya

## Installation Instructions
1) Download this repository to your computer and extract the zip file to any location
2) Copy both ``sfa_o4m.py`` and ``o4m_scripts/`` to your Maya plugin directory. The rest of the files can be deleted
3) Open the maya Plug-in manager window and load the ``sfa_o4m.py`` script.
4) To check that the plugin has loaded correctly, run the command ``o4m_check``. If the plugin is loaded correctly, the command will output the string ``Organise4M is loaded!``.

## Documentation
### o4m_rename
- **Syntax**: ``o4m_rename [mode] [string] [padding]``
- **Function**: Used to rename a selection of objects with a specific format. This command has three 4 modes and a default function where no mode specified.
- **Modes**:
  - ``DEFAULT`` Where no mode is specified, the entire object name will be overriden by the specified string for each object. For example, running ``o4m_rename "BOB" 0`` will replace every object name with ``BOB`` appending a number to prevent duplicates
  - ``-p`` Prefix-mode, prepends the specified string followed by an underscore to each object name. For example, running ``o4m_rename -p "BOB" 0`` on an object ``SMITH`` will result in the name ``BOB_SMITH``
  - ``-pe`` PrefixEdit-mode, replaces everything before the first instance of an underscore with the specified string. For example, running ``o4m_rename -pe "Green" 0`` on an object ``Red_AppleObj_L`` will result in the name ``Green_AppleObj_L``
  - ``s`` Suffix-mode, works the same as Prefix-mode but appends the specified string to the name with a leading underscore. For example, running ``o4m_rename -s "SMITH" 0`` on an object ``BOB`` will result in the name ``BOB_SMITH``
  - ``-se`` SuffixEdit-mode, works the same as PrefixEdit-mode but replaces everything after the last instance of an underscore with the specified string. For example, running ``o4m_rename -se "R"`` on an object ``Green_AppleObj_L`` will result in the name ``Green_AppleObj_R``
- **String format and padding**: String argument must be surrounded by double quotation marks ``"like this"``. Any ``#`` in the string will be replaced with a number (starting at 0) with the specified ``padding``. For example, If you select three objects and run ``o4m_rename "Object#" 2`` the resulting names will be ``Object00``, ``Object01`` and ``Object02``. Here selection order matters. Objects will be named and numbered in the order they are selected. This is useful for bulk renaming objects with numbering. Numbering with ``#`` and padding works with all modes.
### o4m_colour
- **Syntax**: ``o4m_colour [red] [green] [blue]``
- **Function**: Sets the display colour for the all selected nodes to the RGB value specified. Values should be floats between 0 and 1. This command is only useful for shape nodes.
### o4m_getcolour
- **Syntax**: ``o4m_getcolour``
- **Function**: Prints the RGB colour of the selected nodes in the form [red, green, blue, alpha]