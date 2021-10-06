import requests
import os
username = str(os.environ.get("mailaurion"))
password = str(os.environ.get("passaurion"))

urll = 'https://aurion.junia.com/faces/Login.xhtml'
url = 'https://aurion.junia.com/faces/Planning.xhtml'
log = 'https://aurion.junia.com/login'

data = str('username=' + username + '&password=' + password)
print(data)

# https://stackoverflow.com/questions/26615756/python-requests-module-sends-json-string-instead-of-x-www-form-urlencoded-param


##methode POST
rep1 = requests.post(urll, data=data)
rep2 = requests.post(log, data=data)
rep3 = requests.post(url, data=data)
# print(rep1.text)
print(rep1.headers)
# print(rep2.text)
print(rep2.headers)
# print(rep3.text)
print(rep3.headers)

##methode GET
# rep1 = requests.get(urll, data=data)
# rep2 = requests.get(log, data=data)
# rep3 = requests.get(url, data=data)
# # print(rep1.text)
# print(rep1.headers)
# # print(rep2.text)
# print(rep2.headers)
# # print(rep3.text)
# print(rep3.headers)

##methode PUT
# rep1 = requests.put(urll, data=data)
# rep2 = requests.put(log, data=data)
# rep3 = requests.put(url, data=data)
# # print(rep1.text)
# print(rep1.headers)
# # print(rep2.text)
# print(rep2.headers)
# # print(rep3.text)
# print(rep3.headers)