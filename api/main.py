import http.client
import requests
from bs4 import BeautifulSoup

#importation des IDs depuis le PATH (perso)
import os
username = str(os.environ.get("mailaurion"))
password = str(os.environ.get("passaurion"))
baseURL = 'https://aurion.junia.com'

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
    print(resS)
    # print(resH)
    # print(resR.decode('utf-8'))
    return resH


#recuperation du cookie (sous IDs) et parametrage
def cookies(head):
    cookies = ((head).get('Set-Cookie'))
    cookies = str(cookies.rstrip("; Path=/; Secure; HttpOnly"))
    # print(cookies)
    return cookies


#requete GET de la page principale (verification de la presence de PRENOM NOM dans la page print) avec le cookie
def GETmain(cookies,baseURL):
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Cookie': cookies
        }
    tempURL = str(baseURL+'/')
    response = requests.get(tempURL, headers=headers)
    # print(response.text)
    print(response.status_code)
    return response.text


#Recuperation du viewstate creer
def viewS(page):
    soup = BeautifulSoup(page, "html.parser")
    viewS = soup.find("input", {'id': "j_id1:javax.faces.ViewState:0"}).attrs['value']
    # print(viewS)
    return viewS


def GETplanning(cookies,baseURL):
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Cookie': cookies
        }
    tempURL = str(baseURL+"/faces/Planning.xhtml")
    response = requests.get(tempURL, headers=headers)
    # print(response.text)
    # print(response.status_code)
    pass


def POSTmain(viewS, cookies):
    conn = http.client.HTTPSConnection("aurion.junia.com")
    payload = ('''javax.faces.ViewState='''+viewS)
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Cookie': cookies
        }
    conn.request("POST", "/faces/MainMenuPage.xhtml", payload, headers)
    res = conn.getresponse()
    resS = res.status
    resH = res.headers
    resR = res.read()
    print(resS)
    # print(resH)
    # print(resR.decode('utf-8'))
    pass


def POSTplan(viewS, cookies):
    conn = http.client.HTTPSConnection("aurion.junia.com")
    payload = ('''javax.faces.ViewState='''+viewS)
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Cookie': cookies
        }
    conn.request("POST", "/faces/Planning.xhtml", payload, headers)
    res = conn.getresponse()
    resS = res.status
    resH = res.headers
    resR = res.read()
    print(resS)
    # print(resH)
    print(resR)
    pass

