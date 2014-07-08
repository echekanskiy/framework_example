from interface import command
from server_process import is_server_running
import time

class CommandStart(command.AbstractCommand):

    def __init__(self, **kwargs):
        command.AbstractCommand.__init__(self, **kwargs)

    def pre_execute(self):
        pass
        #execute common for windows and linux logic here(like checking if server running or check firewall or anything else)
        #also all common checks, if they platform depended must be dynamically loaded(see server_process module):
        print is_server_running(self.dummy)

    def execute(self):
        print "Starting ambari server"

    def post_execute(self):
        #ensure that server started normally
        print "Waiting for server start..."
        time.sleep(2)
        print "Server started successfully"