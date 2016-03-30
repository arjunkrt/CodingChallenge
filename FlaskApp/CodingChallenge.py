import re
import os

def net_block(ip,subnet):
  ip_bin = '.'.join([bin(int(x)+256)[3:] for x in ip.split('.')])

  subnet_bin = '.'.join([bin(int(x)+256)[3:] for x in subnet.split('.')])

  match_1 = re.search('([\d]+).([\d]+).([\d]+).([\d]+)', ip)
  match_2 = re.search('([\d]+).([\d]+).([\d]+).([\d]+)', subnet)

  r1 = str(int(match_1.group(1))&int(match_2.group(1)))+'.'+str(int(match_1.group(2))&int(match_2.group(2)))+'.'+str(int(match_1.group(3))&int(match_2.group(3)))+'.'+str(int(match_1.group(4))&int(match_2.group(4)))
  
  index = subnet_bin.find("0")
  sub_bin =  subnet_bin[0:index].replace("1","0") + subnet_bin[index:].replace("0","1")
  sub_dec = '.'.join(str(int(x,2)) for x in sub_bin.split('.'))

  match_3 = re.search('([\d]+).([\d]+).([\d]+).([\d]+)', sub_dec)

  r2 = str(int(match_1.group(1))&int(match_3.group(1)))+'.'+str(int(match_1.group(2))&int(match_3.group(2)))+'.'+str(int(match_1.group(3))&int(match_3.group(3)))+'.'+str(int(match_1.group(4))&int(match_3.group(4)))
  return {"network_block": r1,
          "host_id": r2}

def logs(filepath):

  f = open(os.getcwd()+filepath, "rU") 
  first_line = f.readline().rstrip()
  first_line = first_line.split(' ')
  print first_line

#net_block("192.168.2.1","255.255.255.0")
#net_block("192.168.2.1/24")
logs("/logs.txt")

