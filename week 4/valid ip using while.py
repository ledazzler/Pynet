not_done= True
  
while not_done:
  valid_ip = True
  ip_addr = raw_input('enter an ip address:\n')
  octets = ip_addr.split('.')
  
  if '' in octets:
    print 'you entered a blank\n\n'
    continue
  if len(octets) != 4:
    print ('invalid ip - length \n\n')
    continue
  
  if int((octets[0])) <1:
      print 'first octet cannot be 0 or less\n'
      print int((octets[0]))
      valid_ip = False
  elif int((octets[0])) > 223:
      print 'first octet cannot be greater than 223\n'
  elif int((octets[0])) == 127:
      print 'first octet cannot be 127\n'
      valid_ip = False
  else:
    print 'octet 1 is ok\n'
  
  for i in range(1,4):
    if int(octets[i]) < 0:
      print 'octet %d cannot be less than 0 \n' %(i+1)
      valid_ip = False
    elif int(octets[i]) > 255:
      print 'octet %s cannot be greater than 255 \n' %(i+1)
      valid_ip = False
    else:
      print 'octet %s is ok\n' %(i+1)
  
  if int((octets[0])) == 169 and int((octets[1])) == 254:
    print 'first two octets cannot be 169.254'
    valid_ip = False  
    
  if valid_ip == True:
    print 'ip address %s is valid' %ip_addr
    not_done = False
  elif valid_ip == False:
    print 'ip address %s is not valid' %ip_addr
    not_done = True