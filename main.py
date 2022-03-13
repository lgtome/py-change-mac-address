import subprocess
import optparse
import re
from misc.sys import *
from misc.vars import regex
from helpers.get_mac import get_mac_address


    
previous_mac, new_mac, interface = get_mac_address()

def init(prev_mac:str,mac:str,interface:str):
  is_regex_match = re.match(f"{regex}",mac)
  if is_regex_match:
    print('success')
    subprocess.call(f'sudo ifconfig {interface} down',shell=True)
    is_changed = subprocess.call(f'sudo ifconfig {interface} hw ether {mac}',shell=True)
    subprocess.call(f'sudo ifconfig {interface} up',shell=True)
    if not is_changed:
      print(f'previous mac: {prev_mac} turned into -> {new_mac}')
  else: 
    print('New mac address incorrect!')

init(previous_mac,new_mac,interface)