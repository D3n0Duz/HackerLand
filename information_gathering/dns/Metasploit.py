'''
    ######################################
    # Installation
    ######################################

    # wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run && wget https://downloads.metasploit.com/data/releases/metasploit-latest-linux-x64-installer.run.sha1 && echo $(cat metasploit-latest-linux-x64-installer.run.sha1)'  'metasploit-latest-linux-x64-installer.run > metasploit-latest-linux-x64-installer.run.sha1 && shasum -c metasploit-latest-linux-x64-installer.run.sha1 && chmod +x ./metasploit-latest-linux-x64-installer.run && sudo ./metasploit-latest-linux-x64-installer.run

    #####################################
    # Covered modules
    ######################################

    # auxiliary/gather/dns_bruteforce
    # auxiliary/gather/dns_cache_scrapper
    # auxiliary/gather/dns_info
    # auxiliary/gather/dns_reverse_lookup
    # auxiliary/gather/dns_srv_enum


    ######################################
    # How to use metasploit (exemple)
    ######################################

    # Make sure that you have installed the tool
    # Open terminal (Ctrl + Alt + t)
    # msfconsole
    # use auxiliary/gather/dns_reverse_lookup
    # set RANGE <enter the IP of your target>
    # run


'''