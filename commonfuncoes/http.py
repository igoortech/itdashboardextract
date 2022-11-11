import requests

def get(url:str, headers = {}):
    req = requests.get(url, headers=headers)
    print(req.text)
