import requests
import os
from requests.auth import *
from getPlanningXML import getPlanningXML
from requests import Request, Session

username = str(os.environ.get("mailaurion"))
password = str(os.environ.get("passaurion"))

urll = 'https://aurion.junia.com/faces/Login.xhtml'
log = 'https://aurion.junia.com/login'
url = 'https://aurion.junia.com/faces/Planning.xhtml'

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "fr-FR",
"Accept-Encoding": "gzip, deflate, br",
"Content-Type": "application/x-www-form-urlencoded",
"Origin": "https://aurion.junia.com",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User": "?1"}

# data = ("username=" + username + "&password=" + password)
# data = {'username=': username,'&password=': password}
# # print(data)


##methode POST
# rep1 = requests.post(log, data=data, headers=headers)
session = requests.Session()
session.auth = (username,password)

auth = session.post(log)
rep1 = session.get(urll)


# print(rep1.text)
print(rep1.status_code)
print(rep1.headers)



# cookies = ((rep1.headers).get('Set-Cookie'))
# cookies = str(cookies.rstrip("; Path=/; Secure; HttpOnly"))
# print(cookies)

# print(getPlanningXML(url,cookies))