uptime1 = 'twb-sf-881 uptime is 6 weeks, 4 days, 2 hours, 25 minutes'

uptime2 = '3750RJ uptime is 1 hour, 29 minutes'

uptime3 = 'CATS3560 uptime is 8 weeks, 4 days, 18 hours, 16 minutes'

uptime4 = 'rtr1 uptime is 5 years, 18 weeks, 8 hours, 23 minutes'

uptimes = [uptime1,uptime2,uptime3,uptime4]

uptime_dict = {}

sec = 1
mins = 60*sec
hours = 60*mins
days = 24*hours
weeks = 7* days
years = 365*days


string = uptime1.split('uptime is')
hostname = string[0]
time_list = string[1].split(',')
uptime = 0

def uptime_to_seconds(uptime_str):
  string = uptime_str.split('uptime is')
  hostname = string[0]
  time_list = string[1].split(',')
  uptime = 0

  for x in time_list:
    if 'years' in x:
      try:
        uptime += (int(x.split('years')[0])) * years
      except:
        print 'error years'
    elif 'weeks' in x:
      try:
        uptime += (int(x.split('weeks')[0])) * weeks
      except:
        print 'error weeks'
    elif 'days' in x:
      try:
        uptime += (int(x.split('days')[0])) * days
      except:
        print 'error days'      
    elif 'hours' in x:
      try:
        uptime += (int(x.split('hours')[0])) * hours
      except:
        print 'error hours'
    elif 'min' in x:
      try:
        uptime += (int(x.split('minutes')[0])) * mins
      except:
        print 'error minutes'
    elif 'sec' in x:
      try:
        uptime += (int(x.split('seconds')[0])) * sec
      except:
        print 'error seconds'
  
  uptime_dict[hostname] = uptime

#uptime_to_seconds(uptime1)
#print uptime_dict

for uptime in uptimes:
  uptime_to_seconds(uptime)
  
print uptime_dict
