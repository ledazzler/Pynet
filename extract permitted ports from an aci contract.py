#import regex and pretty print
import re
import pprint

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


def quit_fxn():
	not_done= True
  
	while not_done:
		user_input = raw_input('type q to quit:\n')
		if user_input.lower() == 'q':
			not_done = False

aci_contract()
quit_fxn()

