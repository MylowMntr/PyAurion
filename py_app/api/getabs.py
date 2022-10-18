import http.client
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup as soup
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
    return resH

#recuperation du cookie (sous IDs) et parametrage
def Cookies(head):
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
    # print(response.status_code)
    return response.text

#Recuperation du viewstate creer
def ViewState(page):
    soup = BeautifulSoup(page, "html.parser")
    # print(soup)
    viewS = soup.find("input", {'id': "j_id1:javax.faces.ViewState:0"}).attrs['value']
    
    # print(soup)
    menuid = soup.find("span", text="Scolarité")
    # print(menuid)
    menuid = str(menuid.previous_element.previous_element.previous_element.previous_element.previous_element)
    # print(menuid)
    menuid = menuid.split("form:sidebar_menuid':'")
    menuid = menuid[1].split("'})")
    menuid = menuid[0]
    menuid = str( int(menuid) + 1 ) + "_2"
    # print(menuid)
    
    # print(viewS)
    return viewS,menuid

#requete POST de mainpage (pour planning)
def POSTmain(viewS, cookies,baseURL):
    viewS = ViewState(GETmain(cookies,baseURL))[0]
    conn = http.client.HTTPSConnection("aurion.junia.com")
    payload = ("javax.faces.partial.ajax=true&javax.faces.source=form%3Aj_idt52&" +
                "javax.faces.partial.execute=form%3Aj_idt52&javax.faces.partial.render=form%3Asidebar&" +
                "form%3Aj_idt52=form%3Aj_idt52&webscolaapp.Sidebar.ID_SUBMENU=submenu_44413&form=form&" +
                "form%3AlargeurDivCenter=1219&form%3Asauvegarde=&form%3Aj_idt772_focus=&form%3Aj_idt772_input=44323"
                + "&javax.faces.ViewState=" + viewS)
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
    # print(resS)
    # print(resH)
    # print(resR.decode('utf-8'))
    pass

#requete POST de mainpage (pour planning)
def POSTmainn(viewS, cookies,baseURL):
    view = ViewState(GETmain(cookies,baseURL))
    viewS = view[0]
    conn = http.client.HTTPSConnection("aurion.junia.com")
    menuid = view[1]
    payload = ( "form=form&form%3AlargeurDivCenter=1219&form%3Asauvegarde=&" +
                "form%3Aj_idt772_focus=&form%3Aj_idt772_input=44323&" +
                "form%3Asidebar=form%3Asidebar&form%3Asidebar_menuid=" + menuid
                + "&javax.faces.ViewState=" + viewS)
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
    # print(resS)
    # print(resH)
    # print(resR.decode('utf-8'))
    pass

#requete GET avant POST
def GETnote(cookies,baseURL):
    headers = {
        'Content-type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'Cookie': cookies
        }
    tempURL = str(baseURL+"/faces/MesAbsences.xhtml")
    response = requests.get(tempURL, headers=headers)
    # print(response.text)
    # print(response.status_code)


    rep = response.text
    # print(x)
    x = rep.split("Justificatif</span></th></tr></thead>")
    x = x[1].split("</table></div><input type=")
    
    y = rep.split('''<span id="form:dureeAbs" class="Fs14">''')
    y = y[1].split("</span></td>")
    # print(x[0])
    

    xml_data = '''<table>'''+str(x[0])+'''</table>'''

    s = soup(xml_data, 'html.parser')
    result =  [[i.text for i in b.find_all('td')] for b in s.find_all('tr')]    


    return(json.dumps(result, ensure_ascii=False),y[0])
    



def main(username,password):
    # print(username,password)
    baseURL = 'https://aurion.junia.com'
    
    cookies = Cookies(POSTlogin(username,password))
    viewS = ViewState(GETmain(cookies,baseURL))[0]
    
    GETmain(cookies,baseURL)
    POSTmain(viewS,cookies,baseURL)
    POSTmainn(viewS,cookies,baseURL)
    
    return(GETnote(cookies,baseURL))

# print(cookies, viewS)