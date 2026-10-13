import requests

print("requests version:", requests.__version__)
response = requests.get("https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=7")
print(response.json())