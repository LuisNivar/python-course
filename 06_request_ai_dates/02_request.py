import os
import urllib.error
import urllib.request
import json
import requests

os.system("cls")

api_posts = "https://jsonplaceholder.typicode.com/posts/"
# 1- Without dependencies
# try:
#     response = urllib.request.urlopen(api_posts)
#     data = response.read()
#     json_data = json.loads(data.decode("utf-8"))
#     print(json_data)
#     response.close()
# except urllib.error.URLError as e:
#     print(f"Error in the request: {e}")

    
# 2- With a dependency 
# pip install requests

# GET
print("="*80)
print("/GET")
print("-"*80)
response = requests.get(url=api_posts)
data = response.json()
print(data[0:3])

# GET - Indentation
print("="*80)
print("/GET")
print("-"*80)
response = requests.get(url=api_posts)
data = response.json()
print(json.dumps(data[0:2], indent=2))

# POST
print("="*80)
print("/POST")
print("-"*80)
input = {
    "title": 'foo',
    "body": 'bar',
    "userId": 2, 
}
try:
    response = requests.post(url=api_posts, json=input)
    data = response.json()
    print(data)
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Request error: {e} ") 
print("-"*80)

# POST
print("="*80)
print("/PUT")
print("-"*80)
input = {
    "title": 'foo',
    "body": 'bar',
    "userId": 2, 
}
try:
    response = requests.put(url="https://jsonplaceholder.typicode.com/posts/1", json=input)
    data = response.json()
    print(data)
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Request error: {e} ") 
print("-"*80) 