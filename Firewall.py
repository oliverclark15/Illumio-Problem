import csv
import re
from collections import defaultdict

class Firewall:
	
	def __init__(self, path):
		self.rules_dict = defaultdict(list)
		with open(path) as file:
			rules = csv.reader(file,delimiter=',')
			for rule in rules:
				self.rules_dict[rule[0]+"-"+rule[1]].append((rule[2],re.sub('[.]', '', rule[3])))
		#print(self.rules_dict)		

	def check_range(self, range_p, packet_value):
		val_range = range_p.split("-")
		if (packet_value >= int(val_range[0]) and packet_value <= int(val_range[1])):
			return True
		return False


	def accept_packet(self, direction, protocol, port, ip_address):
		rkey = direction+"-"+protocol
		# Check the list of rules associated with packets
		# unique direction/protocol combination (of which there are four).
		for rule in self.rules_dict[rkey]:
			port_rule = rule[0]
			addr_rule = rule[1]
			ip_address = re.sub('[.]','',ip_address)
			if("-" in port_rule):
				if(not self.check_range(port_rule,port)): 
					continue # Try next rule
			else:
				if((port) != int(port_rule)):
					continue # Try next rule

			if("-" in addr_rule):
				if(not self.check_range(addr_rule,int(ip_address))):
					continue # Try next rule
			else:
				if(ip_address != addr_rule):
					continue # Try next rule
			return True # Match found!

		return False
