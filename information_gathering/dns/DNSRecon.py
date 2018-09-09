import socket

from utility.ExecuteTerminal import execute_terminal

# from utility.SaveResults import save_results
from utility.Seperators import seperator_single_line

'''
    # https://github.com/darkoperator/dnsrecon.git
    
    # Git clone dnsrecon
    # git clone https://github.com/darkoperator/dnsrecon.git
    
    # Install python packages
    # pip install netaddr
    # pip install dnspython
    # pip install lxml
    
'''


class DNSRecon:
    def __init__(self, url, dnsrecon_path):
        self.url = url
        self.dnsrecon_path = dnsrecon_path
        self.result = self.execute_dnsrecon_zonetransfer()
        self.result += seperator_single_line
        self.result += self.execute_dnsrecon_bruteforce()
        self.result += seperator_single_line
        self.result += self.execute_dnsrecon_reverse_ptr()

    # Gives dns zone transfer
    def execute_dnsrecon_zonetransfer(self):
        command = self.dnsrecon_path + "dnsrecon.py -a -d " + str(self.url).replace('www.', '')
        return execute_terminal("dnsrecon-zonetransfer", command)

    # Brute forces to discover
    def execute_dnsrecon_bruteforce(self):
        command = self.dnsrecon_path + "dnsrecon.py -t brt -d " + str(self.url).replace('www.', '')
        return execute_terminal("dnsrecon-bruteforce", command)

    # Brute forces to discover
    def execute_dnsrecon_reverse_ptr(self):
        command = self.dnsrecon_path + "dnsrecon.py -r " + str(socket.gethostbyname(str(self.url))) + "/24"
        return execute_terminal("dnsrecon-reverse-ptr", command)

    def get_results(self):
        return self.result


# v = DNSRecon("www.google.com", "/home/neo/Workspace/DNSRecon/dnsrecon/")

# save_results(str(v.get_results()), "/home/neo/Workspace/HackerLand/information_gathering", "dnsrecon1.txt")
