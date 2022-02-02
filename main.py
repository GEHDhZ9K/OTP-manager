#!/usr/bin/env python3

import os, json, sys

os.chdir(os.path.dirname(sys.argv[0]))

name = input(str("Enter the name: "))
secret = input(str("Enter the secret: "))

def write_dict(data, file="./data/storage.json"):
  with open(file, "w") as f:
    json.dump(data, f,indent=2)

def append_dict(file="./data/storage.json"):
  with open(file, "r") as f:
    f_load = json.load(f)
    f_keys = f_load["keys"]
    f_keys[name] = secret
    return f_load
