#!/usr/bin/env python3

import os, json, sys

path = os.path.abspath(__file__).split("/")[0:-1]
if os.getcwd() != "/".join(path):
  os.chdir(os.path.dirname(sys.argv[0]))

name = "name1"
secret = "secret1"

def create_json():
  with open("./data/storage.json", "w") as f:
    data = {"credential": {"password": "test"}, "keys" :{}}
    json.dump(data, f, indent=2)

if "data" not in os.listdir():
  os.mkdir("data")
  create_json()
elif "storage.json" not in os.listdir("data"):
  create_json()

def write_json(data, file="./data/storage1.json"):
	with open(file, "w") as f:
		json.dump(data, f, indent=2)

def append_dict(prev, new):
	prev_keys = prev["keys"]
	prev_keys[new[0]] = new[1]
	return prev

def read_json(file="./data/storage.json"):
	with open(file, "r") as f:
		f_load = json.load(f)
		return f_load

def encrypt(name="name3", secret="secret3"):
  name_l = "".join([chr(ord(i) << 2) for i in name])
  secret_l = "".join([chr(ord(i) << 2) for i in secret])
  return name_l, secret_l

def decrypt(file="./data/storage.json"):
	name_l, secret_l = [], []
	with open(file, "r") as f:
		f_load = json.load(f)
		f_keys = f_load["keys"]
		for key in f_keys:
			name_l.append("".join([chr(ord(i) >> 2) for i in key]))
			secret_l.append("".join([chr(ord(j) >> 2) for j in f_keys.get(key)]))
	return dict(zip(name_l, secret_l))

def check_pass(passw, file="./data/storage.json"):
  with open(file) as f:
    f_load = json.load(f)
    f_cred = f_load['credentials']
    for i in f_cred:
      if f_cred.get(i) == "test" and passw == "test":
        return True
      elif f_cred.get(i) == "test" and passw != "test":
        return False
      else:
        if passw == "".join([chr(ord(j) >> 2) for j in f_cred.get(i)]):
          return True
        else:
          return False