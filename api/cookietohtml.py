import requests

url = 'https://aurion.junia.com/faces/Planning.xhtml'

cookie = {'JSESSIONID': cookie,}
response = requests.get(url, cookies=cookie)

print(response.text)

