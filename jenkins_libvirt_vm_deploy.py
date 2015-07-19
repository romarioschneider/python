#!/bin/python

import subprocess
import sys
import os

def ex_remote_command(routeros_addr, ssh_key, routeros_port, routeros_user, command_line, grep_expr, cut_column):
    cmd = ['ssh -p {0} -i {1} {2}@{3} "{4}" | grep {5} | cut -d " " -f {6}'.format(routeros_port, ssh_key, routeros_user, routeros_addr, command_line, grep_expr, cut_column)]

    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    r_code = proc.wait()
    if r_code != 0:
        print("[ERROR] execute command filed!")
        return None
    results = proc.communicate()
    
    return results
    
def get_free_port (start_port, stop_port):
    
    out_list = ex_remote_command('172.22.22.222', '/var/lib/jenkins/.ssh/id_dsa', '50022', 'jenkins', 'ip firewall nat print chain=dstnat', 'dst-port', 9)[0].split("\n")
    list_ports = []
    for i in out_list:
        if i != '':
            tmp = i.split("=")
            list_ports.append(int(tmp[1]))
    list_ports_sorted =  sorted(list_ports)
    #print(list_ports_sorted)
    
    i = 0
    left_position = None
    while i <= stop_port:
        if start_port <= list_ports_sorted[i] <= stop_port:
            left_position = i
            break
        i = i + 1
    #print(list_ports_sorted[left_position - 1:])
    
    i = start_port
    while i <= stop_port:
        if i not in list_ports_sorted[left_position - 1:]:
            return i
        i = i + 1
    return False

print(get_free_port(sys.argv[1], sys.argv[2]))
