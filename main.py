import subprocess
import optparse
import re
from misc.vars import regex
from misc.sys import *


def get_mac_address():
  interface = input('Enter interface: ')
  if not interface:
    exit('Interface must be provided!')
  ifconfig_res = subprocess.check_output(['ifconfig',interface]).decode()
  regex_res = re.findall(f"{regex}",ifconfig_res)
  mac_address = ''
  for i in range(0,4):
    mac_address += regex_res[i]
  if not mac_address:
    exit('Mac address not found')
  else:
    new_mac_address = input('Enter new mac address: ')
    return [mac_address,new_mac_address,interface]

    
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