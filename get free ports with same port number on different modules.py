import pprint

ports = [
  
  "XGE1/7/0/2    ",  
"XGE1/7/0/16   ",  
"XGE1/8/0/5    ",  
"XGE1/8/0/7    ",  
"XGE1/8/0/9    ",  
"XGE1/8/0/10   ",  
"XGE1/8/0/11   ",  
"XGE1/8/0/12   ",  
"XGE1/8/0/14   ",  
"XGE1/8/0/19   ",  
"XGE1/8/0/20   ",  
"XGE1/9/0/2    ",  
"XGE1/9/0/3    ",  
"XGE1/9/0/4    ",  
"XGE1/9/0/6    ",  
"XGE1/9/0/8    ",  
"XGE1/9/0/9    ",  
"XGE1/9/0/26   ",  
"XGE1/9/0/27   ",  
"XGE1/9/0/28   ",  
"XGE1/9/0/29   ",  
"XGE1/9/0/30   ",  
"XGE1/9/0/31   ",  
"XGE1/9/0/32   ",  
"XGE1/9/0/33   ",  
"XGE1/9/0/34   ",  
"XGE1/9/0/35   ",  
"XGE1/9/0/36   ",  
"XGE1/9/0/37   ",  
"XGE1/9/0/38   ",  
"XGE1/9/0/39   ",  
"XGE1/9/0/40   ",  
"XGE2/7/0/2    ",  
"XGE2/7/0/16   ",  
"XGE2/8/0/5    ",  
"XGE2/8/0/6    ",  
"XGE2/8/0/7    ",  
"XGE2/8/0/9    ",  
"XGE2/8/0/10   ",  
"XGE2/8/0/12   ",  
"XGE2/8/0/14   ",  
"XGE2/8/0/19   ",  
"XGE2/8/0/20   ",  
"XGE2/9/0/2    ",  
"XGE2/9/0/3    ",  
"XGE2/9/0/4    ",  
"XGE2/9/0/6    ",  
"XGE2/9/0/8    ",  
"XGE2/9/0/9    ",  
"XGE2/9/0/26   ",  
"XGE2/9/0/27   ",  
"XGE2/9/0/28   ",  
"XGE2/9/0/29   ",  
"XGE2/9/0/30   ",  
"XGE2/9/0/31   ",  
"XGE2/9/0/32   ",  
"XGE2/9/0/33   ",  
"XGE2/9/0/34   ",  
"XGE2/9/0/35   ",  
"XGE2/9/0/36   ",  
"XGE2/9/0/37   ",  
"XGE2/9/0/38   ",  
"XGE2/9/0/39   ",  
"XGE2/9/0/40   ",  
]


ports = [x.strip() for x in ports]

module1 = []
module2 = []

dup_ports =[]

#x = ports[1]
#print x
#print x.split('/')[0]
#print x.split('/')[1:]

for i in ports:
  if i.split('/')[0] == 'XGE1':
    module1.append(i)
  elif i.split('/')[0] == 'XGE2':
    module2.append(i)

for x in module1:
  a = x.split('/')[1:]
  for i in module2:
    if i.split('/')[1:] == a:
      print 'match at %s' %i





#x = ports[1]
#print x.split('/')[1:]
#a = x.split('/')[1:]
#print ','.join(a)
