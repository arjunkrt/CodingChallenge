import re
import os
import datetime
import time
import socket

#Function to validate Date
def validate(input):
  try:
    datetime.datetime.strptime(input, '%Y-%m-%d')
    return "Valid"
  except ValueError:
    return "Invalid"

#Function to validate Time
def isTimeFormat(input):
  try:
    time.strptime(input, '%H:%M:%S,%f')
    return "Valid"
  except ValueError:
    return "Invalid"

#Function to validate the IP address
def validate_ip(input):
  a = input.split('.')
  if len(a) != 4:
    return False
  for row in a:
    if not row.isdigit():
      return False
    i = int(row)
    if i < 0 or i > 255:
      return False
  return True

#Function which calculate Network Block and Host ID from IP adddress and Subnet Mask
def net_block(ip,subnet):
#validate the IP address
  if validate_ip(ip) and validate_ip(subnet):
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


#Function to find the valid logs from the given input
def logs(input_string):
  #Approved log level list
  log_list = ['ERROR','INFO','DEBUG']
  final_string = '<Date> <Log Level> <User> <Main Function> <Sub Function> <Logged Message>\n'
  for row in input_string.splitlines()[1:]:

    flag = 0
    i = 1
    row_string = re.sub( '\s+', ' ', row ).strip()
    message = row_string.split("]")[1][1:]
    ms = re.search('([\w\d\s\-]+)\s+([\w:,]+)\s+([\w]+)\s+([\w\s\]\[\:\_]+)\s+', row_string)
    if ms is not None:
      date = ms.group(1)
      res = validate(date)

    #Date validation
      if res == 'Invalid':
        flag = 1

      time = ms.group(2)
      time_res = isTimeFormat(time)

      #Time validation
      if time_res == 'Invalid':
        flag = 1

      log_level = ms.group(3)
      string = ms.group(4)
      string = string.split("]")
      user_data = string[0].split(":")
      user = user_data[0][1:]

    #Checking for User validation
      if (' ' in user) == True:
        flag = 1
      function = user_data[1]
      sub_func = ''
      if len(user_data) == 3:
        sub_func = ' ' + user_data[2]

    #Log level validation
      if log_level not in log_list:
        flag = 1

      if flag == 0: 
        final_string += date + ' ' + time + ' ' + log_level + ' ' + user + ' ' + function + sub_func + ' ' + message + '\n'

  return {"valid_logs": final_string}
  

#net_block('192.168.2.1','255.255.255.0')
#logs(string)

