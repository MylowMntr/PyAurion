
import requests
import os
username = str(os.environ.get("mailaurion"))
password = str(os.environ.get("passaurion"))

urll = 'https://aurion.junia.com/faces/Login.xhtml/login'
ulr = 'https://aurion.junia.com/login'
url = 'https://aurion.junia.com/faces/Planning.xhtml'

data = {'username': username,'password': password}
rep1 = requests.post(ulr, data=data)

# print(rep1.text)
print(rep1.headers)

cookies = ((rep1.headers).get('Set-Cookie'))
cookies = cookies.rstrip("; Path=/; Secure; HttpOnly")
cookies = cookies.split("=")
cookies = {cookies[0]:cookies[1]}
print(cookies)

rep2 = requests.post(url, cookies=cookies)


# print(rep1.text)
# print(rep1.cookies)
# print(rep2.text)
print(rep2.cookies)
