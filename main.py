#!/usr/bin/env python3

import os, json, sys

path = os.path.abspath(__file__).split("/")
del path[-1]
if os.getcwd() != "/".join(path):
  os.chdir(os.path.dirname(sys.argv[0]))

name = input(str("Enter the name: "))
secret = input(str("Enter the secret: "))

def create_json():
  with open("./data/storage.json", "w") as f:
    data = {"keys" :{}}
    json.dump(data, f, indent=2)


if "data" not in os.listdir():
  os.mkdir("data")
  create_json()
elif "storage.json" not in os.listdir("data"):
  create_json()

def write_dict(data, file="./data/storage.json"):
  with open(file, "w") as f:
    json.dump(data, f,indent=2)

def append_dict(file="./data/storage.json"):
  with open(file, "r") as f:
    f_load = json.load(f)
    f_keys = f_load["keys"]
    f_keys[name] = secret
    return f_load
