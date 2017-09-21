list_ip = []
while len(list_ip) != (3) and len(list_ip) !=4:
  ip_addr = str(raw_input("enter the ip address:"))
  list_ip = ip_addr.split(".")
  final_list = []
  final_str = ''
  a = "NETWORK_NUMBER"   
  b = "FIRST_OCTET_BINARY"       
  c = "FIRST_OCTET_HEX"
  
  if len(list_ip) != (3) and len(list_ip) !=4:
    print "invalid value"
    print len(list_ip)
  else:
    final_list.append(list_ip[0])
    final_list.append(list_ip[1])
    final_list.append(list_ip[2])
    final_list.append(0)
    final_str = str(final_list[0]) +'.' + str(final_list[1]) +'.' + str(final_list[2]) + '.' + str(final_list[3])
    
    
    print 'subnet is %s.%s.%s.%s' %(final_list[0],final_list[1],final_list[2],final_list[3])
    print ""
    print "%20s %20s %20s" %(a,b,c)
    print "%20s %20s %20s" %(final_str, bin(int(final_list[0])), hex(int(final_list[1])))