import subprocess

from utility.Seperators import seperator_single_line
from utility.TextColors import print_green, print_red


# Execute terminal commands
def execute_terminal(tool_name, cmd):
    print_green("[!] Starting %s ..." % tool_name)
    output = ""
    try:
        cmd = cmd.rstrip()
        output += subprocess.checkout_output(cmd, shell=True, stderr=subprocess.STDOUT)
        output += "\r\n"
    except Exception as e:
        print_red("[!] Error: Executing the command " + cmd + " Reasons:\r\n" + str(e))
        output += "\r\n"
    output += seperator_single_line + "\r\n"
    print_green("[+] Finished %s ..." % tool_name)
    return output
