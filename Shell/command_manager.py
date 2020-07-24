# Managing user commands one at a time, handling display

import threading
import datetime as datetime
from .commands import Commands

# Class implements Thread to ease usage as it will always be launched as a new thread
class CommandManager(threading.Thread):
    def __init__(self,command,args=(),kwargs=None):
        threading.Thread.__init__(self,args=(),kwargs=None)
        # time_start will be used to measure performances
        self.time_start = datetime.datetime.now()
        self.counter_retry = 0
        # function object to be executed. this is ensure by Cmd module and therefore may not be checked
        self.command = command
        # friendly name for function object to be executed
        self.command_name = command.__name__
        # args for function
        self.args = args
    
    # Thread core, handle display. 
    # Synchronization of display between threads may be challenging and Tasks may be considered if display synchronization is required
    def run(self):
        print("RECEIVED: " + self.command_name + " AT " + str(self.time_start.strftime("%H:%M:%S.%f")) + " WITH PARAMS " + str(self.args))
        try:
            # Desired function will be executed here, all error handling must be done in command itself
            print("EXECUTED: " + self.command_name + " RESULTS: " + str(self.command(self.args)) + " - ELAPSED TIME: " + str(datetime.datetime.now() - self.time_start))
        
        # Is only raised if a plugin developper handled errors badly
        except:
            print("ERROR: " + self.command_name)

            