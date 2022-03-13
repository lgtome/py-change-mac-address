import subprocess
import re
from misc.vars import regex

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
