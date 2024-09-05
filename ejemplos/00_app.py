"""
curl -X POST http://localhost:11434/api/generate -d '{
"model": "tinyllama",
"prompt": "Why is the sky blue?",
"stream": false
}'
"""

import requests
import json

url = 'http://localhost:11434/api/generate'

while True:
    prompt = input ("PROMPT: ")

myobj = {
"model": "tinyllama",
"prompt": prompt,
"stream": False
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers = headers)

response = json.loads(response.text)
"""|
x = requests.post(url, json = myobj)
x = json.loads(x.text)
"""
print(x["response"])


