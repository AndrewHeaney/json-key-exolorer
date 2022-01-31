import sys
import inquirer
import json
import os
import argparse

os.system('cls' if os.name == 'nt' else 'clear')


parser = argparse.ArgumentParser(
  prog='jkx', 
  description='Select which JSON file to explore',
  epilog='Example: jkx openapi.json'
)
parser.add_argument('-f', action="store", dest="file")
args = parser.parse_args()

f = open(args.file)
data = json.load(f)

nodes = []

def gen_array_keys(array):
  index_array = []
  for i in range(len(array)):
    index_array.append(i)
  
  return index_array

def explore_json(json_data):
  keys = []
  if (type(json_data) == list):
    keys = gen_array_keys(json_data)
  else:
    for key, value in json_data.items():
      keys.append(key + ' (' + str(type(value)).split("'")[1] + ')')

  questions = [
      inquirer.List('key',
        message="Select a key from the JSON data",
        choices=keys,
      ),
    ]

  answer = inquirer.prompt(questions)
  if (type(answer['key']) == str):
    next_key = answer['key'].split(' ')[0]
  else:
    next_key = answer['key']

  nodes.append(next_key)

  print(gen_path())
  
  if (type(json_data[next_key]) != str):
    explore_json(json_data[next_key])

def gen_path():
  path = "Path = /"
  for node in nodes:
    path += str(node) + '/'
  return path

def start():
  explore_json(data)

if __name__ == "__main__":
   start()