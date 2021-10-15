import http.client
import os
username = str(os.environ.get("mailaurion"))
password = str(os.environ.get("passaurion"))

conn = http.client.HTTPSConnection("aurion.junia.com")

headers = ('''
    Connection: keep-alive
    Content-type: application/x-www-form-urlencoded

    username{'''+username+'''}
    &password{'''+password+'''}
        ''')
conn.request("POST", "/login", headers)
res = conn.getresponse()
data = res.headers
datar = res.read()
print(data)

cookies = ((data).get('Set-Cookie'))
cookies = str(cookies.rstrip("; Path=/; Secure; HttpOnly"))
print(cookies)


headers = ('''
        Cookie: '''+cookies+'''
    ''')

conn.request("GET", "/", headers)

res = conn.getresponse()
data = res.headers
datar = res.read()
print(data)

