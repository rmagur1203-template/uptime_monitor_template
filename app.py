import requests
import os
import json
import datetime

print(os.environ)

try:
  remote = os.environ.get('SERVICE_DOMAIN')
except:
  remote = input()
try:
  limit = int(os.environ.get('STORE_LIMIT'))
except:
  limit = int(input())

try:
  f = open('uptime.json', 'r')
  data = json.load(f)
  f.close()
except:
  data = []

res = requests.get(remote)

data.append({'code': res.status_code, 'text': res.text, 'date': datetime.datetime.now().isoformat()})
data = data[-limit:]
print(data)

f = open('uptime.json', 'w')
json.dump(data, f)
f.close()
