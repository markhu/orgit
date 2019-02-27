#!/usr/bin/python

import json
import sys

verbs=["CREATE","LIST","MOVE","DELETE"]

# data={"faked":"element","el-top":{"el-mid":"child"}}
data = json.loads(open("data.json",'r').read())

try:
  v=sys.argv[1]
except:
  v="undef-verb"

try:
  o=sys.argv[2]
  # ToDo: parse slashes to dict
  
except:
  o=data

if v in verbs:
    print("Command: {}".format(v))
else:
    print("Supported commands: {}".format(verbs))
#    exit(1)

def process_commands(v,o):
  if v.upper() in "LIST":
      print("LIST")
      print(dict_to_lines(o))
  print("process end")
  return 0

def dict_to_lines(data,padding='  '):
    lines=[]
    for k in data:
      lines.append(k)
      # print("DEBUG: {}".format(data[k]))
      if type(data[k]) is dict:
        lines.append( padding + dict_to_lines(data[k],padding + padding))
      else:
        lines.append( padding + data[k])
    text=''
    for line in lines:
       text += "{}\n".format(line)
    return(text)

process_commands(v,o)

