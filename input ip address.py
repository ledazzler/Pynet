list_ip = []
while len(list_ip) != (3) and len(list_ip) !=4:
  ip_addr = str(raw_input("enter the ip address:"))
  list_ip = ip_addr.split(".")
  final_list = []
  if len(list_ip) != (3) and len(list_ip) !=4:
    print "invalid value"
    print len(list_ip)
  else:
    final_list.append(list_ip[0])
    final_list.append(list_ip[1])
    final_list.append(list_ip[2])
    final_list.append(0)
    
    
    
    print 'subnet is %s.%s.%s.%s' %(final_list[0],final_list[1],final_list[2],final_list[3])