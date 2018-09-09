from utility.ExecuteTerminal import execute_terminal


# from utility.SaveResults import save_results


class Nslookup:
    def __init__(self, url):
        self.url = url
        self.result = self.execute_whois()

    def execute_whois(self):
        command = "nslookup " + str(self.url).replace('www.', '')
        return execute_terminal("nslookup", command)

    def get_results(self):
        return self.result

# v = Nslookup("www.google.com")

# save_results(str(v.get_results()), "/home/neo/Workspace/HackerLand/information_gathering", "nslookup1.txt")
