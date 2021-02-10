import requests

r = requests.get('http://192.168.0.103:8081')
if r.status_code == requests.codes.ok:
    print("OK")

print(r.text)
