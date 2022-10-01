
import socket

def scan(target, ports):
	print('\n' + ' Starting Scan for ' + str(target))
	for port in range(1, ports):
		scan_port(target, port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Open Port: "+ str(port))
		sock.close()
	except:
		pass


targets = input("[*] Enter the ip address (seperate by ,): ")
ports = int(input("[*] How many ports do you want?: "))

if ',' in targets:
	print("[*] Scanning multiple targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
