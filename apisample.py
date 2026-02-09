import requests

# URL of a large file (for demo purposes, a sample text file)
url = "https://www.w3.org/"

# Ask the server for only the first 100 bytes
headers = {"Range": "bytes=0-99"}
response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)  # should be 206
print("Response Headers:", response.headers)
print("Partial Content:\n", response.text)

