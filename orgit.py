#!/usr/bin/python

import json
import sys

verbs=["CREATE","LIST","MOVE","DELETE"]

# data={"faked":"element","el-top":{"el-mid":"child"}}
f = open("data.json","r")
data = json.loads(f.read())

try:
  v=sys.argv[1].upper()
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
  if v in "CREATE":
      print("CREATE " + o)
      elements = o.split('/')
      do_create(elements)
  elif v in "MOVE":
      print("MOVE " + o)
      elements = o.split(' ')  # space-delimited args
      do_move(elements)
  elif v in "DELETE":
      print("DELETE " + o)
      elements = o.split('/')
      do_delete(elements)
  return 0

def do_delete(elements):  # side-effect(s) on global data dict
      top = elements[0]
      data[top] = {}

def do_move(elements):  # side-effect(s) on global data dict
      top = elements[0]
      tip = elements[len(elements)-1]
      data[top] = tip


def do_create(elements):  # side-effect(s) on global data dict
      top = elements[0]
      if len(elements) == 2:
        tip = elements[len(elements)-1]
        data[top] = tip
      elif len(elements) == 3:  # ToDo: fix this kludge and properly recurse!
        tip = elements[len(elements)-1]
        twig = elements[len(elements)-2]
        data[top] = {}
        data[top][twig] = tip
      else:
        tip = {}
        data[top] = tip


def dict_to_lines(data,padding='  '):
    lines=[]
    for k in data:
      lines.append(k)
      # print("DEBUG: {}".format(data[k]))
      if type(data[k]) is dict:
        lines.append( padding + dict_to_lines(data[k],padding + padding))
      else:
        if len(data[k]) > 1:  # childless
          lines.append( padding + data[k])

    text=''
    for line in lines:
       text += "{}\n".format(line)

    return(text)

process_commands(v,o)

if v in "LIST":
  print("LIST")
  print(dict_to_lines(o))
else:
  f = open("data.json","w")
  f.write(json.dumps(data)+"\n")
