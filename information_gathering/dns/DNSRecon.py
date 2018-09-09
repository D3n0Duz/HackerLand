from utility.ExecuteTerminal import execute_terminal

# from utility.SaveResults import save_results

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
        self.result = self.execute_dnsrecon()

    def execute_dnsrecon(self):
        command = self.dnsrecon_path + "dnsrecon.py -a -d " + str(self.url).replace('www.', '')
        return execute_terminal("dnsrecon", command)

    def get_results(self):
        return self.result


# v = DNSRecon("www.google.com", "/home/neo/Workspace/DNSRecon/dnsrecon/")

# save_results(str(v.get_results()), "/home/neo/Workspace/HackerLand/information_gathering", "dnsrecon1.txt")
