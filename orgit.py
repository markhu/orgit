#!/usr/bin/python

import sys

verbs=["CREATE","LIST","MOVE","DELETE"]

data={"faked":"element"}  # ToDo: read from .JSON file

try:
  v=sys.argv[1]
except:
  v="undef-verb"

try:
  o=sys.argv[2]
except:
  o="undef-object"

if v in verbs:
    print("Command: {}".format(v))
else:
    print("Supported commands: {}".format(verbs))
#    exit(1)

def process_commands(v,o):
  if v.upper() in "LIST":
    for line in data:
      print("{}/{}".format(line, data[line]))
  print("process end")
  return 0


process_commands(v,o)

