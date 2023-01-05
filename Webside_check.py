import requests

Error = [404, 505, 400]

r = requests.get("https://monitoring.cloud.1home.io")

print(r.ok)
print(r.status_code)

if r.status_code == Error:
    print("Webside not working") 