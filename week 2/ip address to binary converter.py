list_ip = []
while len(list_ip) != (3) and len(list_ip) !=4:
  ip_addr = str(raw_input("enter the ip address:"))
  list_ip = ip_addr.split(".")
  final_list = []
  final_str = ''
  a = "first_octet"   
  b = "second_octet"       
  c = "third_octet"
  d = "fourth_octet"
  
  if len(list_ip) != (3) and len(list_ip) !=4:
    print "invalid value"
    print len(list_ip)
  else:
    final_list.append(list_ip[0])
    final_list.append(list_ip[1])
    final_list.append(list_ip[2])
    final_list.append(0)
    final_str = str(final_list[0]) +'.' + str(final_list[1]) +'.' + str(final_list[2]) + '.' + str(final_list[3])
    
    
    print "%20s %20s %20s %20s" %(a,b,c,d)
    print "%20s %20s %20s %20s" %(bin(int(final_list[0])), bin(int(final_list[1])), bin(int(final_list[2])), bin(int(final_list[3])))