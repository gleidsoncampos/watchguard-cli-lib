import time
from connection import connection

NOT_FOUND =-1
class runCommand:
    def __init__(self, conn, debug):
        self.conn = conn
        self.debug = debug
    
    def exe(self, command):
        buff_size=2024
        c=command + '\n'
        self.conn.channel.send(c)

        #wait for results to be buffered
        while not (self.conn.channel.recv_ready()):
            if self.conn.channel.exit_status_ready():
                print ('Channel exiting. No data returned')
                return
            time.sleep(5) 

        #print results 
        while self.conn.channel.recv_ready():
            output=self.conn.channel.recv(buff_size)
            if self.debug:
                print(output)

        #WatchGuard errors have ^ in output
        #throw an exception if we get a WatchGuard error
        if output.find('^')!=NOT_FOUND or output.find('Error')!=NOT_FOUND:
            while output.find('master')!=NOT_FOUND:
                self.escape
            raise ValueError('Error executing firebox command: ' + output, command)
            
        return output

    def escape(self):
        a = True

        while (a):
            buff_size=2024
            c = 'exit \n'
            self.conn.channel.send(c)

            #wait for results to be buffered
            while not (self.conn.channel.recv_ready()):
                if self.conn.channel.exit_status_ready():
                    print ('Channel exiting. No data returned')
                    return
                time.sleep(5) 

            #print results 
            while self.conn.channel.recv_ready():
                output=self.conn.channel.recv(buff_size)
                if output.find('master')==NOT_FOUND:
                    a = False
                if self.debug:
                    print(output)
            
        return output