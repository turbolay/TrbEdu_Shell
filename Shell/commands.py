# List of commands.
# Commands must be implemented in modules extensions
# worldtimeapi is given as an extension example

from Shell.Extensions.worldtimeapi import WorldTimeApi as worldtimeapi
from Shell.Extensions.dofutils import DofUtils as dofutils

class Commands():
    # initialization of all function libraries that can be called as user inputed commands
    def __init__(self):
        # To load extension just call constructor
        self.worldtimeapi = worldtimeapi()
        self.dofutils = dofutils()