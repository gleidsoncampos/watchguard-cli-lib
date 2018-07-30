import boto3
import paramiko
import time
import logging
from botocore.client import Config

NOT_FOUND =-1

class connection:
    #local channel used to run commands
    channel=None
    sshclient=None

#    logging.getLogger('paramiko').setLevel(logging.DEBUG)

    def __init__(self):
        pass

    def open_connection(self, sshpass, sshuser, fireboxip, sshport):

        clone=self
#        print ('try to connect to Firebox')
        try:

            clone.sshclient = paramiko.SSHClient()
            #override check in known hosts file
            #https://github.com/paramiko/paramiko/issues/340
            clone.sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            clone.sshclient.connect( hostname = fireboxip, port = sshport, username = sshuser, password = sshpass)
            clone.channel = clone.sshclient.invoke_shell()

        except:
            print ('cannot connect to firebox')
            raise

        print('connected to ' + fireboxip)


    def close_connections(self):
        if self.channel:
            self.channel.close()
            print ('channel closed')
        
        if self.sshclient:
            self.sshclient.close()
            print ('connection closed')