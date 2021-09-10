import requests

print("Requests version is " + requests.__version__)
response = requests.get("https://www.google.com/")
print(response.status_code)
