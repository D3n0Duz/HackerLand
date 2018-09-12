'''
    #############
    # Download
    #############
    # git clone https://github.com/laramies/theHarvester.git
    #
    # (I cloned it here : /home/neo/Workspace/TheHarvester/theHarvester/)
'''


from utility.ExecuteTerminal import execute_terminal


# from utility.SaveResults import save_results


class TheHarvester:
    def __init__(self, url, theharvester_path):
        self.url = url
        self.theharvester_path = theharvester_path
        self.result = self.execute_theharvester()

    def execute_theharvester(self):
        command = "python " + self.theharvester_path + "theHarvester.py -d " + str(self.url).replace("www.", "") + " -b all"
        return execute_terminal("theharvester", command)

    def get_results(self):
        return self.result


# v = TheHarvester("www.google.com", "/home/neo/Workspace/TheHarvester/theHarvester/")

# save_results(str(v.get_results()), "/home/neo/Workspace/HackerLand/information_gathering", "nslookup1.txt")