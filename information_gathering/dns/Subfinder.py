import os

'''
    # https://github.com/subfinder/subfinder
    
    # Install Go Language
    # sudo apt install gccgo - go
    # sudo apt  install golang-go

    # Install subfinder
    # go get github.com/subfinder/subfinder

    # Update subfinder
    # go get -u github.com/subfinder/subfinder

    # Git clone subfinder
    # git clone https://github.com/subfinder/subfinder.git

    # Set up subfinder
    # sh build.sh
    # go build

    #(I cloned it here ./Workspace/Subfinder/subfinder)
'''


class Subfinder:
    def __init__(self, url, need_output_txt_file, subfinder_path, file_path, file_name):
        self.url = url
        self.subfinder_path = subfinder_path
        self.file_path = file_path
        self.file_name = file_name

        if need_output_txt_file is False:
            self.result = self.execute_subfinder()
        else:
            self.result = self.execute_subfinder_with_output()

    # Run subfinder
    def execute_subfinder(self):
        command = self.subfinder_path + " -d " + str(self.url).replace("www.", "") + " -v"
        return os.system(command)

    # Run subfinder and create output file
    def execute_subfinder_with_output(self):
        path = self.file_path + "/" + self.file_name
        command = self.subfinder_path + " -d " + str(self.url).replace("www.", "") + " -v -o " + path
        return os.system(command)

    # Use multiple threads (10 in this exemple)
    def execute_subfinder_intense(self):
        command = self.subfinder_path + " -d " + str(self.url).replace("www.", "") + " -v -t 10"
        return os.system(command)

    def execute_subfinder_help(self):
        command = self.subfinder_path + " -h"
        return os.system(command)

    def get_results(self):
        return self.result


'''v = Subfinder("www.google.com", False, "/home/neo/Workspace/Subfinder/subfinder/subfinder",
              "/home/neo/Workspace/HackerLand/information_gathering", "subfinder1.txt")
'''

'''
#v = Subfinder("www.google.com", True, "/home/neo/Workspace/Subfinder/subfinder/subfinder",
              "/home/neo/Workspace/HackerLand/information_gathering", "subfinder1.txt")
'''
