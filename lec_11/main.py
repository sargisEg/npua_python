import requests

def filter_by_title(data):
  filtered = []
  for single_data in data:
    if len(single_data["title"]) <= 20:
            filtered.append(single_data)
  return filtered

def filter_by_desc_lines(data):
  filtered = []
  for single_data in data:
    if single_data["body"].count('\n') >= 3:
            filtered.append(single_data)
  return filtered

def do_post(url):
  data = {
    "title": "Foo",
    "body": "Bar",
    "userId": 12
  }
  response = requests.post(url, data)
  if response.status_code == 201:
    return response.json()
  else:
    return response.status_code

def do_put(url, id):
  data = {
    "title": "Foo",
    "body": "Bar",
    "userId": 12
  }
  response = requests.put(url + "/" + str(id), data)
  if response.status_code == 200:
    return response.json()
  else:
    return response.status_code

def do_delete(url, id):
  requests.delete(url + "/" + str(id))
  return response.status_code

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

print(filter_by_title(data))
print(filter_by_desc_lines(data))
print(do_post(url))
print(do_put(url, 15))
print(do_delete(url, 15))
