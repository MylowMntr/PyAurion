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
    # print(viewS)
    return viewS

#requete POST de mainpage (pour planning)
def POSTmain(viewS, cookies,baseURL):
    viewS = ViewState(GETmain(cookies,baseURL))
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
    viewS = ViewState(GETmain(cookies,baseURL))
    conn = http.client.HTTPSConnection("aurion.junia.com")
    menuid = "1_1"
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
    tempURL = str(baseURL+"/faces/ChoixIndividu.xhtml")
    response = requests.get(tempURL, headers=headers)
    # print(response.text)
    # print(response.status_code)
    return response.text

def POSTnote(viewS, cookies,baseURL):
    viewS = ViewState(GETnote(cookies,baseURL))
    start = str(0)
    rows = str(10000)
    # payload = ("javax.faces.partial.ajax=true&javax.faces.source=form%3Aj_idt149&javax.faces.partial.execute=form%3AdivRecherche&"
    #             + "javax.faces.partial.render=form%3AdataTableFavori&form%3Aj_idt149=form%3Aj_idt149&form=form&form%3AlargeurDivCenter=1603&form%"
    #             + "3AmessagesRubriqueInaccessible=&form%3Asearch-texte=&form%3Asearch-texte-avancer=&form%3Ainput-expression-exacte=&form%3Ainput-un-des-mots=&"
    #             + "form%3Ainput-aucun-des-mots=&form%3Ainput-nombre-debut=&form%3Ainput-nombre-fin=&form%3Aj_idt133_input=PeriodePersonnalisee&form%"
    #             + "3AcalendarDebut_input=01%2F01%2F20&form%3AcalendarFin_input=31%2F01%2F30&form%3Aj_idt181_reflowDD=0_0&form%3Aj_idt181%3Aj_idt255%3Afilter=&"
    #             + "form%3Aj_idt181%3Aj_idt257%3Afilter=&form%3Aj_idt181%3Aj_idt259%3Afilter=&form%3Aj_idt181%3Aj_idt261%3Afilter=&form%3Aj_idt181%3Aj_idt263%3Afilter=&"
    #             + "form%3Aj_idt181%3Aj_idt265%3Afilter=&form%3Aj_idt242_focus=&form%3Aj_idt242_input=44323"
    #             + "&javax.faces.ViewState="+ urllib.parse.quote(viewS))
    
    payload = ("javax.faces.partial.ajax=true&javax.faces.source=form%3Aj_idt181&" +
                "javax.faces.partial.execute=form%3Aj_idt181&javax.faces.partial.render=form%3Aj_idt181&" +
                "form%3Aj_idt181=form%3Aj_idt181&form%3Aj_idt181_pagination=true&" +
                "form%3Aj_idt181_first=" + start +
                "&form%3Aj_idt181_rows=" + rows +
                "&form%3Aj_idt181_skipChildren=true&form%3Aj_idt181_encodeFeature=true&" +
                "form=form&form%3AlargeurDivCenter=835&form%3AmessagesRubriqueInaccessible=&form%3Asearch-texte=&" +
                "form%3Asearch-texte-avancer=&form%3Ainput-expression-exacte=&form%3Ainput-un-des-mots=&" +
                "form%3Ainput-aucun-des-mots=&form%3Ainput-nombre-debut=&form%3Ainput-nombre-fin=&" +
                "form%3AcalendarDebut_input=&form%3AcalendarFin_input=&form%3Aj_idt181_reflowDD=0_0&" +
                "form%3Aj_idt181%3Aj_idt186%3Afilter=&form%3Aj_idt181%3Aj_idt188%3Afilter=&" +
                "form%3Aj_idt181%3Aj_idt190%3Afilter=&form%3Aj_idt181%3Aj_idt192%3Afilter=&" +
                "form%3Aj_idt181%3Aj_idt194%3Afilter=&form%3Aj_idt181%3Aj_idt196%3Afilter=&form%3Aj_idt254_focus=&" +
                "form%3Aj_idt254_input=44323"+ "&javax.faces.ViewState="+ urllib.parse.quote(viewS))
    # print(payload)
    
    conn = http.client.HTTPSConnection("aurion.junia.com")
    headers = { "Accept": "application/xml, text/xml, */*; q=0.01",
                "Host": "aurion.junia.com",
                "Accept-Language": "fr-FR",
                "Accept-Encoding": "gzip, deflate, br",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Faces-Request": "partial/ajax",
                "X-Requested-With": "XMLHttpRequest",
                "Connection": "keep-alive",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                'Cookie': cookies
        }
    conn.request("POST", "/faces/ChoixIndividu.xhtml", body=payload, headers=headers, encode_chunked=True)
    res = conn.getresponse()
    resS = res.status
    resH = res.headers
    resR = res.read()
    # print(resS)
    # print(resH)
    x = resR.decode('utf-8')
    x = x.split("[CDATA[")
    x = x[3].split("]]")
    return(x[0])
    



def main(username,password):
    # print(username,password)
    baseURL = 'https://aurion.junia.com'
    
    cookies = Cookies(POSTlogin(username,password))
    viewS = ViewState(GETmain(cookies,baseURL))
    
    GETmain(cookies,baseURL)
    POSTmain(viewS,cookies,baseURL)
    POSTmainn(viewS,cookies,baseURL)
    GETnote(cookies,baseURL)
    
    return(POSTnote(viewS,cookies,baseURL))

# main()
# print(cookies, viewS)