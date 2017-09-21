import pprint

routes = """<?xml version="1.0" encoding="UTF-8"?><imdata totalCount="1"><l3extRsNodeL3OutAtt dn="uni/tn-DC2B-TRS/out-L3_Out_Static_Internal/lnodep-L3_Out_Static_Internal_Node/rsnodeL3OutAtt-[topology/pod-1/node-201]" rtrId="10.77.224.10" rtrIdLoopBack="no" tDn="topology/pod-1/node-201"><ipRouteP aggregate="no" descr="" ip="10.76.93.0/24" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.229.208/28" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.92.0/24" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.75.128.0/17" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.236.0/24" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.88.0/23" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.237.0/24" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="104.219.106.132/32" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.238.0/24" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="104.219.107.134/32" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.77.0.0/16" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.100.96/28" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.96.0/23" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.234.0/23" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.232.0/23" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP><ipRouteP aggregate="no" descr="" ip="10.76.90.0/23" name="" nameAlias="" pref="1" rtCtrl=""><ipNexthopP descr="" name="" nameAlias="" nhAddr="10.77.254.14" pref="unspecified" type="prefix"/></ipRouteP></l3extRsNodeL3OutAtt></imdata>"""

rlist = routes.split('ip=')
subnets = []
junk = []

for i in rlist:
  subnets.append(i.split()[0])
  junk.append(i.split()[1:])


#for i in junk:
#  for thing in i:
#    if '10' in thing:
#      print thing


#print a
#print a.split()[0]
#print '*********'
#print a.split()[1:]

for i in subnets:
  print i