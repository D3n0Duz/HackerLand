from utility.ExecuteTerminal import execute_terminal


# from utility.SaveResults import save_results


class WhoIs:
    def __init__(self, url):
        self.url = url
        self.result = self.execute_whois()

    def execute_whois(self):
        command = "whois " + self.url
        return execute_terminal("whois", command)

    def get_results(self):
        return self.result

# v = WhoIs("google.com")

# save_results(str(v.get_results()), "/home/neo/Workspace/HackerLand/information_gathering", "whois1.txt")
