from runCommand import runCommand

class sslMobileVpn:
    def __init__(self, conn, debug):
        self.conn = conn
        self.debug = debug
        self.commnand = runCommand(self.conn, self.debug) 
        #enter configure mode
        c = 'configure'
        self.commnand.exe(c)
        #enter policy mode
        c = 'policy'
        self.commnand.exe(c)
    
    def addUserRoute (self, ip_or_net=[]):
        #command to add routes or ips to vpn
        for ip in ip_or_net:
            c = 'sslvpn resource user-route ' + ip
            self.commnand.exe(c)
        self.commnand.exe('apply')
        self.commnand.escape()
    
    def removeUserRoute (self, ip_or_net=[]):
        #command to remove routes or ips from vpn
        for ip in ip_or_net:
            c = 'no sslvpn resource user-route ' + ip
            self.commnand.exe (c)
        self.commnand.exe('apply')
        self.commnand.escape()