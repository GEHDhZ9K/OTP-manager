#!/usr/bin/env python3

import os, json, sys

path = os.path.abspath(__file__).split("/")[0:-1]
if os.getcwd() != "/".join(path):
  os.chdir(os.path.dirname(sys.argv[0]))

def encryption_func(value):
  return "".join([chr(ord(i) << 2) for i in str(value)])

def decryption_func(value):
  return "".join([chr(ord(i) >> 2) for i in str(value)])

def create_json():
  with open("./data/storage.json", "w") as f:
    data = {"credential": {"password": "ǐƔǌǐ"}, "keys" :{}}
    json.dump(data, f, indent=2)

if "data" not in os.listdir():
  os.mkdir("data")
  create_json()
elif "storage1.json" not in os.listdir("data"):
  create_json()

def write_json(data, file="./data/storage.json"):
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

def encrypt(name, secret):
  name_l = encryption_func(name)
  secret_l = encryption_func(secret)
  return name_l, secret_l

def decrypt(file="./data/storage.json"):
	name_l, secret_l = [], []
	with open(file, "r") as f:
		f_load = json.load(f)
		f_keys = f_load["keys"]
		for key in f_keys:
			name_l.append(decryption_func(key))
			secret_l.append(decryption_func(f_keys.get(key)))
	return dict(zip(name_l, secret_l))

def check_pass(passw, file="./data/storage.json"):
  with open(file) as f:
    f_load = json.load(f)
    f_cred = f_load['credential']["password"]
    if passw == decryption_func(f_cred):
      return True
    else:
      return False

def change_pwd(text, file="./data/storage.json"):
  with open(file) as f:
    f_load = json.load(f)
    encoded = encryption_func(text)
    f_load["credential"]["password"] = encoded
  with open(file, "w") as fp:
    json.dump(f_load, fp, indent=2)

def write_to_file(name, secret):
  write_json(append_dict(read_json(), encrypt(name, secret)))