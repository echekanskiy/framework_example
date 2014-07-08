
import interface.start
import sys

def _execute_command(command):
    command.pre_execute()
    command.execute()
    command.post_execute()

def main(argv):
    #handle all args here(can copy this from original ambari-server.py), pass all arguments to constructor,
    #we get start command in this example with args dummy="dummy"}
    command_str = "start"
    args = {"dummy":"dummy"}
    command = None
    if command_str == "start":
        command = interface.start.CommandStart(dummy="dummy")

    _execute_command(command)

if __name__ == "__main__":
    main(sys.argv)