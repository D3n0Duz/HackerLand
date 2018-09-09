import socket

from utility.ExecuteTerminal import execute_terminal


# from utility.SaveResults import save_results
from utility.Seperators import seperator_single_line

'''
    # Install whois
    # sudo apt-get install nmap
'''


class Nmap:
    def __init__(self, url):
        self.url = url
        self.result = self.execute_nmap_zonetransfer()
        self.result += seperator_single_line
        self.result += self.execute_nmap_bruteforce()
        self.result += seperator_single_line
        self.result += self.execute_nmap_reverse_ptr()

    def execute_nmap_zonetransfer(self):
        command = "nmap --script=dns-zone-transfer " + str(self.url).replace('www.', '')
        return execute_terminal("nmap-zonetransfer", command)

    def execute_nmap_bruteforce(self):
        command = "nmap --script=dns-brute " + str(self.url).replace('www.', '')
        return execute_terminal("nmap-zonetransfer", command)

    def execute_nmap_reverse_ptr(self):
        command = "nmap -sL " + str(socket.gethostbyname(str(self.url))) + "/24"
        return execute_terminal("nmap-reverse", command)

    def get_results(self):
        return self.result


# v = Nmap("www.google.com")

# save_results(str(v.get_results()), "/home/neo/Workspace/HackerLand/information_gathering", "nmap1.txt")
