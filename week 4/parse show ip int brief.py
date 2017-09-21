show_ip_int_brief = '''

Interface            IP-Address      OK?     Method      Status     Protocol

FastEthernet0   unassigned      YES     unset          up          up

FastEthernet1   unassigned      YES     unset          up          up

FastEthernet2   unassigned      YES     unset          down      down

FastEthernet3   unassigned      YES     unset          up          up

FastEthernet4    6.9.4.10         YES     NVRAM       up          up

NVI0                  6.9.4.10        YES     unset           up          up

Tunnel1            16.25.253.2     YES     NVRAM       up          down

Tunnel2            16.25.253.6     YES     NVRAM       up          down

Vlan1                unassigned      YES    NVRAM       down      down

Vlan10              10.220.88.1     YES     NVRAM       up          up

Vlan20              192.168.0.1     YES     NVRAM       down      down

Vlan100            10.220.84.1     YES     NVRAM       up          up

'''
int_list = show_ip_int_brief.split('\n')
int_list = filter(None,int_list)

int_tuple_list = []


for i in int_list[1:-1]:
  a = i.split()
  if 'up' in a[-2] and 'up' in a[-1]:
    intf,ip,junk1,junk2,line,prot = a
    int_tuple_list.append((intf,ip,line,prot))
    

for i in int_tuple_list:
  print i
  print '\n'
