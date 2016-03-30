import re
import os
import datetime

def validate(date_text):
  try:
    datetime.datetime.strptime(date_text, '%Y-%m-%d')
  except ValueError:
    #raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    return "Invalid"

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
  #print first_line
  #ms = re.findall('([\w]+)\s+([\w]+)', first_line)
  log_list = ['ERROR','INFO','DEBUG']
  for row in f:
    #print row.rstrip()
    flag = 0
    row_string = re.sub( '\s+', ' ', row ).strip()
    message = row_string.split("]")[1][1:]
    ms = re.search('([\w\d\s\-]+)\s+([\w:,]+)\s+([\w]+)\s+([\w\s\]\[\:\_]+)\s+', row_string)
    date = ms.group(1)
    res = validate(date)
    if res == 'Invalid':
      flag = 1
    time = ms.group(2)
    log_level = ms.group(3)
    string = ms.group(4)
    string = string.split("]")
    user_data = string[0].split(":")
    user = user_data[0][1:]
    function = user_data[1]
    sub_func = ''
    if len(user_data) == 3:
      sub_func = user_data[2]

    if log_level not in log_list:
      flag = 1
      print 'Invalid log'

    if flag == 0:
      string = date + log_level + user + function + sub_func + message
      print row

logs("/logs.txt")

