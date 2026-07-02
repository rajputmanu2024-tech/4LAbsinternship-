import json

File="data/students.json"

def load_data():
    with open(File, 'r') as f:
        data = json.load(f)
    return data


def save_data(data):
  with open(File,'w') as f:
    json.dump(data,f)