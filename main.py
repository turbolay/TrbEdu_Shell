# Main class for program with commands loop using Cmd module

import cmd,sys
import time
from Shell.commands import Commands as commands
from Shell.command_manager import CommandManager as cm

# Cmd object
cmdHandler = None

# Cmd class, will handle all commands passed from user using module Cmd 
class CmdHandler(cmd.Cmd):
    # TrbEdu.commands module
    commands = commands()
    # Cmd util functions, each function will create an available command for the interactive shell
    def do_timezonetotime(self, tz):
        # Help for command. Handled by Cmd module
        """usage: timezonetotime [timezone]
        Get time from timezone - default: return time for timezone associated with user ip"""
        # Create a command manager with requested command, pass args and start execution as a new thread
        cm(self.commands.worldtimeapi.timezonetotime,args=(tz)).start()

    # Alias for better user experience
    def do_tz_t(self, tz):
        """usage: tz_t [timezone]
        alias for timezonetotime - Get time from timezone - default: return time for timezone associated with user ip"""
        self.do_timezonetotime(tz)

    def do_iptotime(self, ip):
        """usage: iptotime [ip]
        Get time for timezone associated with given IP - default: user ip"""
        cm(self.commands.worldtimeapi.iptotime,args=(ip)).start()

    def do_ip_t(self, ip):
        """usage: ip_t [ip]
        alias for iptotime - Get time for timezone associated with given IP - default: user ip"""
        self.do_iptotime(ip)
    
    # See Cmd module for advanced usage and keywords like stop
    def do_close(self,stop):
        """close
        quit programm"""
        return True

    def do_posportails(self,server):
        """usage: pos [server]
        Get dimension position for given server"""
        cm(self.commands.dofutils.posportails,args=(server)).start()

if __name__ == "__main__":
    print("Cmd")
    # Remove (Cmd) default prompt as display must be handled by command_manager module
    cmd.PROMPT=''
    # Start Cmd internal event loop to catch and dispatch user inputs as commands
    cmdLoop = CmdHandler().cmdloop()