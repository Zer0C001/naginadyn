#!/usr/bin/python
import sys
f=open('/var/run/inadyn/inadyn.cache','r')
inadyn_ip=f.read()
ips={'k':(),'w':()}
nextarg=''
for arg in sys.argv:
	if nextarg!='' and arg!='':
		ips.update({nextarg:arg.split(',')})
	if arg=='-k':
		nextarg='k'
	elif arg=='-w':
		nextarg='w'
	else:
		nextarg=''	
if inadyn_ip in ips['k']:
	print 'ok: current ip: '+inadyn_ip
	exit(0)
elif (inadyn_ip in ips['w']) or ips['w']==():
	print 'warn: current ip: '+inadyn_ip
	exit(1)
else:
	print 'err: current ip: '+inadyn_ip
	exit(2)
