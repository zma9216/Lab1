import requests

print("Requests version is " + requests.__version__)
response_1 = requests.get("https://www.google.com/")
print(response_1.status_code)

response_2 = requests.get("https://raw.githubusercontent.com/zma9216/Lab1/main/lab1.py")
print("\n" + response_2.text)
