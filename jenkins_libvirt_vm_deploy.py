#!/bin/python

import subprocess
import sys
import os

def ex_remote_command(routeros_addr, ssh_key, routeros_port, routeros_user, command_line, grep_expr, cut_column):
    cmd = ['ssh -p {routeros_port} -i {ssh_key} {routeros_user}@{routeros_addr} "{command_line}" | grep {grep_expr} | cut -d " " -f {cut_column}'.format(routeros_port=routeros_port, ssh_key=ssh_key, 
				routeros_user=routeros_user, routeros_addr=routeros_addr, command_line=command_line, grep_expr=grep_expr, cut_column=cut_column)]

    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    r_code = proc.wait()
    if r_code != 0:
        print("[ERROR] execute command filed!")
        return None
    results = proc.communicate()
    
    return results #return list with shell-process output
    
#Processing list with int values and return unused port. Need range of TCP/UDP ports
def get_free_port (start_port, stop_port):
    
    input_values = ex_remote_command('172.22.22.222', '/var/lib/jenkins/.ssh/id_dsa', '50022', 'jenkins', 'ip firewall nat print chain=dstnat', 'dst-port', 9)[0].split("\n")
    list_ports = []
    for i in input_values:
        if i != '':
            list_ports.append(int(i.split("=")[1]))  #Parsing lines e. g. "dst-port=21"
        
    list_ports_sorted =  sorted(list_ports)
    
    i = 0
    left_position = None
    while i < len(list_ports_sorted):
        if start_port <= list_ports_sorted[i] <= stop_port: #Finding first entry in specified port range on GW dst-nat table
            left_position = i
            break
        i = i + 1
    
    #Getting free IP port from specified range
    i = start_port
    while i <= stop_port:
        if i not in list_ports_sorted[left_position - 1:]:
            return i
        i = i + 1
    return False

print(get_free_port(int(sys.argv[1]), int(sys.argv[2])))
