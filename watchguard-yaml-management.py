import yaml, os, sys
from connection import connection
from sslMobileVpn import sslMobileVpn

credentials ={}
task_arguments ={}
yamlFile = sys.argv[1:].__str__().strip("[']")

for key, value in yaml.load(open(yamlFile))['credentials'].iteritems():
    credentials[key]=value
#print (credentials.get("user"))

for key, value in yaml.load(open(yamlFile))['task_arguments'].iteritems():
    task_arguments[key]=value
#print (task_arguments)

conn = connection()


conn.open_connection(credentials.get('sshpass'), credentials.get('sshuser'),credentials.get('fireboxip'), credentials.get('sshport'))

#add ssl VPN user Route
if (task_arguments.get('function') in'addSSLVPNUserRoute'):
    command = sslMobileVpn (conn, task_arguments.get('debug_mode'))
    command.addUserRoute(task_arguments.get('net_or_ips'))

#remove ssl VPN user Route
if (task_arguments.get('function') in'removeSSLVPNUserRoute'):
    command = sslMobileVpn (conn, task_arguments.get('debug_mode'))
    command.removeUserRoute(task_arguments.get('net_or_ips'))