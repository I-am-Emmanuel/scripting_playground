import requests

url = 'https://api.pwnedpasswords.com/range/' + '3C49F'
result = requests.get(url)
print(result)