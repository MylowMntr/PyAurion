import http.client
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import urllib
import pytz
import json


#Requete POST avec http.client (ne fonctionne pas avec requests)
def POSTlogin(username,password):
    conn = http.client.HTTPSConnection("aurion.junia.com")
    payload = ('''username='''+username+'''&password='''+password+'''&j_idt28=''')
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive"
        }
    conn.request("POST", "/login", payload, headers)
    res = conn.getresponse()
    resS = res.status
    resH = res.headers
    resR = res.read()
    # print(resS)
    # print(resH)
    # print(resR.decode('utf-8'))
    return resS

def main(sem,username,password):
    #importation des IDs depuis le user.json
    baseURL = "https://aurion.junia.com"
    
    if (POSTlogin(username,password) == 302):
        return True
    else: 
        return False
    
    
# print(main(0,"milo.montuori%40student.junia.com","5%3F8xWrAg"))