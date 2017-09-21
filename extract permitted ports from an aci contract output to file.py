#import regex, pretty print and datetime
import re
import pprint
import datetime

#function will prompt for input - you should paste xml download of filter here
def aci_contract():
  contract = raw_input('please enter contract info: \n')
  print '\n' * 20
  #split string into lines
  output = contract.split('>')
  	
  new_out = []
  junk = []
  
  #this for loop looks for string that identifies beginning of service, then strips out service and removes trailing backslash
  for i in output:
    if 'tnVzFilterName=' in i:
    	#print 'match %s' %i
    	y = re.search(r'(tnVzFilterName=)(.+)',i)
    	y = y.group(2)
    	y = y.strip('/')
    	new_out.append(y)
    else:
    	junk.append(i)
  	
  
  print 'list of permitted services is: \n'
  for i in new_out:
    pprint.pprint(i)
  
  print '\n\n\n' + '<'*10 + '>'*10
  print '\n XML file entries that was not detected as a service: \n'
  for i in junk:
  	  pprint.pprint(i)

  date = datetime.datetime.now().strftime('%Y-%m-%d')
  time = datetime.datetime.now().strftime('%H:%M:%S')
    
  date = date.replace('-','_')
  time = time.replace(':','_')
  
  date_str = 'contract_output' + '_' +  date + '_' + time + '.txt'
  
  with open(date_str,'ab+') as f:
  f.write('list of permitted services is: \r\n')
  f.write('<' * 20)
  f.write('>' * 20 + '\r\n')
  f.write('\r\n\n')
  for i in new_out:
  	f.write(i + '\r\n')

aci_contract()


