#!/usr/bin/env python3

import os, json, sys

path = os.path.abspath(__file__).split("/")[0:-1]
if os.getcwd() != "/".join(path):
  os.chdir(os.path.dirname(sys.argv[0]))

name = "name5"
secret = "secret5"

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

def read_dict(file="./data/storage.json"):
  with open(file, "r") as f:
    f_load = json.load(f)
  return f_load

def encryption(name, secret):
  return dict(zip([chr(ord(i) << 2) for i in name], [chr(ord(i) << 2) for i in secret]))
  
def decryption(file="./data/storage.json"):
  with open(file) as f:
    f_loaded = json.load(f)
    f_keys = f_loaded['keys']
    json_keys = {}
    for key in f_keys:
      json_keys["".join([chr(ord(_i) >> 2) for _i in key])] = "".join([chr(ord(_a) >> 2) for _a in f_keys.get(key)])
  return json_keys

def check_pass(token, file="./data/storage.json"):
  with open(file) as f:
    f_loaded = json.load(f)
    f_keys = f_loaded["credentials"]
    passw = "".join([chr(ord(_i) >> 2) for _i in f_keys.get("password")])
    if f_keys.get("password") == "test" and token == "test":
      return True
    elif f_keys.get("password") == "test" and token != "test":
      return False
    else:
      if token == passw:
        return True
      else:
        return False
