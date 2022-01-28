from operator import index
import sys
import inquirer
import json

f = open(sys.argv[1])
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
    for key in json_data:
      keys.append(key)

  questions = [
      inquirer.List('key',
        message="Select a key from the JSON data",
        choices=keys,
      ),
    ]

  answer = inquirer.prompt(questions)
  next_key = answer['key']
  nodes.append(next_key)
  
  if (type(json_data[next_key]) != str):
    explore_json(json_data[next_key])

def gen_path():
  path = "Path = /"
  for node in nodes:
    path += str(node) + '/'
  return path

explore_json(data)
print(gen_path())
