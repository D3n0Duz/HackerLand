import subprocess

from utility.Seperators import seperator_single_line
from utility.TextColors import print_green, print_red


# Execute terminal commands
def execute_terminal(tool_name, cmd):
    print_green("[!] Starting %s ..." % tool_name)
    print("\r\n" + seperator_single_line + "\r\n")
    output = ""
    try:
        output += str(subprocess.check_output(cmd.rstrip(), shell=True, stderr=subprocess.STDOUT), 'utf-8')
        print(output)
    except Exception as e:
        print_red("[!] Error: Executing the command '" + cmd + "' \r\nReasons: " + str(e))
    print("\r\n" + seperator_single_line + "\r\n")
    print_green("[+] Finished %s ..." % tool_name)
    return output
