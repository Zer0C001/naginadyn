#!/usr/bin/python
import sys
import socket
f=open('/var/run/inadyn/inadyn.cache','r')
inadyn_ip=f.read()
f.close()
ips={'k':(),'w':(),'h':()}
host_ip=''
nextarg=''
exit_st=0
host_msg=''
for arg in sys.argv:
	if nextarg!='' and arg!='' and arg!='-k' and arg!='-w' and arg!='-h':
		ips.update({nextarg:arg.split(',')})
	elif arg=='-k':
		nextarg='k'
	elif arg=='-w':
		nextarg='w'
	elif arg=='-h':
		nextarg='h'
	else:
		nextarg=''	
if len(ips['h'])>1:
	host_msg='warn: not resolving multiple hostnames'
	exit_st=1
elif len(ips['h'])==1:
	host_ip=socket.gethostbyname(ips['h'][0])
	if host_ip==inadyn_ip:
		host_msg='hostname: ok'
	else:
		host_msg='hostname( '+ips['h'][0]+' ): wrong ip: '+host_ip
		exit_st=1
if inadyn_ip in ips['k']:
	if host_msg=='':
		print 'ok: current ip: '+inadyn_ip
	else:
		print 'ok: current ip: '+inadyn_ip+' ; '+host_msg
	exit(exit_st)
elif (inadyn_ip in ips['w']) or ips['w']==():
	if host_msg=='':
		print 'warn: current ip: '+inadyn_ip
	else:
		print 'warn: current ip: '+inadyn_ip+' ; '+host_msg
	exit(1)
else:
	if host_msg=='':
		print 'err: current ip: '+inadyn_ip
	else:
		print 'err: current ip: '+inadyn_ip+' ; '+host_msg
	exit(2)
