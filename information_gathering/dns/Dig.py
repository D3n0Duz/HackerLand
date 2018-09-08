from utility.ExecuteTerminal import execute_terminal


# from utility.SaveResults import save_results
from utility.SaveResults import save_results
from utility.Seperators import seperator_single_line


class Dig:
    def __init__(self, url, ip):
        self.url = url
        self.ip = ip
        self.result = self.execute_dig()
        self.result += seperator_single_line
        self.result += self.execute_dig_ns()
        self.result += seperator_single_line
        self.result += self.execute_dig_mx()
        self.result += seperator_single_line
        self.result += self.execute_dig_trace()
        self.result += seperator_single_line
        self.result += self.execute_dig_reverse_trace()
        self.result += seperator_single_line
        self.result += self.execute_dig_any()
        self.result += seperator_single_line
        self.result += self.execute_dig_axfr()
        self.result += seperator_single_line
        self.result += self.execute_dig_soa()

    # Gives the IP, CNAME and TTL (if there is 2 IP , there is load balancing)
    def execute_dig(self):
        command = "dig " + self.url
        return execute_terminal("dig", command)

    # Gives the subdomain names and IP (A for IPv4 , AAAA for IPv6)
    def execute_dig_ns(self):
        command = "dig ns " + str(self.url).replace('www.', '')
        return execute_terminal("dig-ns", command)

    # Gives the mail server names, priorities and IP
    def execute_dig_mx(self):
        command = "dig mx " + str(self.url).replace('www.', '')
        return execute_terminal("dig-mx", command)

    # Gives DNS client, recursive resolver, root server and authoritative server
    def execute_dig_trace(self):
        command = "dig +trace " + str(self.url).replace('www.', '')
        return execute_terminal("dig-trace", command)

    # Gives DNS client, special referal, recursive resolver, root server and authoritative server (maps IP to name:PTR)
    def execute_dig_reverse_trace(self):
        command = "dig +trace -x " + self.ip
        return execute_terminal("dig-reverse-trace", command)

    # Gives any discovered names
    def execute_dig_any(self):
        command = "dig " + str(self.url).replace('www.', '') + " -t any"
        return execute_terminal("dig-any", command)

    # Gives zone transfer
    def execute_dig_axfr(self):
        command = "dig " + str(self.url).replace('www.', '') + " -t axfr"
        return execute_terminal("dig-axfr", command)

    # Gives the serial number
    def execute_dig_soa(self):
        command = "dig " + str(self.url).replace('www.', '') + " -t soa"
        return execute_terminal("dig-soa", command)

    def get_results(self):
        return self.result

#v = Dig("www.google.com", "8.8.8.8")

#save_results(str(v.get_results()), "/home/neo/Workspace/HackerLand/information_gathering", "dig1.txt")
