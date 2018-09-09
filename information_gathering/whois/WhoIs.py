from utility.ExecuteTerminal import execute_terminal


# from utility.SaveResults import save_results

'''
    # Install whois
    # apt-get install whois
'''


class WhoIs:
    def __init__(self, url):
        self.url = url
        self.result = self.execute_whois()

    def execute_whois(self):
        command = "whois " + str(self.url).replace('www.', '')
        return execute_terminal("whois", command)

    def get_results(self):
        return self.result

# v = WhoIs("www.google.com")

# save_results(str(v.get_results()), "/home/neo/Workspace/HackerLand/information_gathering", "whois1.txt")
