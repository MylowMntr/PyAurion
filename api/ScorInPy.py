import http.client
import requests
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import urllib
import pytz

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

#Recuperation du viewstate creer
def ViewState(page):
    soup = BeautifulSoup(page, "html.parser")
    # print(soup)
    viewS = soup.find("input", {'id': "j_id1:javax.faces.ViewState:0"}).attrs['value']
    # print(viewS)
    return viewS

#Recup des MenuID (sidebar)
def MenuID(page, text):
    soup = BeautifulSoup(page, "html.parser")
    menuID = str(soup.findAll("a", text=text))
    # print(menuID)
    menuID = menuID.split(",'form:sidebar_menuid':'")
    menuID = menuID[1].split("'})")
    menuID = menuID[0]
    print(menuID)
    return menuID

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

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    viewS = soup.find("input", {'id': "j_id1:javax.faces.ViewState:0"}).attrs['value']
    # print(viewS)

    menuID = str(soup.findAll("a", text="Mon Planning"))
    menuID = menuID.split(",'form:sidebar_menuid':'")
    menuID = menuID[1].split("'})")
    menuID = menuID[0]
    # print(menuID)
    return [viewS, menuID, response.text]

#requete GET avant POST
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
    
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    viewS = soup.find("input", {'id': "j_id1:javax.faces.ViewState:0"}).attrs['value']
    # print(viewS)

    formID = "117"
    return [viewS, formID, response.text]

#requete POST de mainpage (pour planning)
def POSTmain(cookies, viewS):
    viewS, menuID, res = GETmain(cookies,baseURL)
    conn = http.client.HTTPSConnection("aurion.junia.com")
    payload = ('''form=form&form%3AlargeurDivCenter=1219&form%3Asauvegarde=&form%3Aj_idt772_focus=&form%3Aj_idt772_input=44323&form%3Asidebar=form%3Asidebar&form%3Asidebar_menuid='''
                + str(menuID)
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
    print(resS)
    # print(resH)
    # print(resR.decode('utf-8'))
    pass

def POSTplanA(cookies):
    #Nbr de la semaine actuelle
    d = date.today()
    # print(d)
    year_number = d.isocalendar()[0]
    week_number = d.isocalendar()[1]
    # print(week_number+1)

    #Chercher la date du lundi de la semaine actuelle
    Monday = d - timedelta(days=d.weekday())
    monday = str(Monday)
    monday = datetime.strptime(monday,"%Y-%m-%d").strftime("%d/%m/%Y")
    monday = monday.replace("/","%2F")

    #date du lundi en Milliseconde
    Monday = Monday.strftime("%d.%m.%Y")+' 00:00:00,00'
    Monday = int((datetime.strptime(Monday,'%d.%m.%Y %H:%M:%S,%f')).timestamp()* 1000)
    # print(Monday)

    #calcul de l'offset 
    tz = datetime.now()
    timezone = pytz.timezone("Europe/Paris")
    tz = timezone.localize(tz)
    tz = (int(tz.utcoffset() / timedelta(hours=1)))*3600000
    # print(tz)

    #date en Milliseconde du lundi (start) et du samedi (end)
    start = Monday
    end = Monday + (6*24*60*60*1000)
    # print(start, end)

    #Mise en forme avant concatenation
    year_number = str(year_number)
    week_number = str(week_number)
    start = str(start)
    end = str(end)
    formID = "117"
    tz = str(-tz)
    # print(start, end)
    
    viewS, menuID, res = GETmain(cookies,baseURL)
    print(viewS, menuID, formID)

    POSTmain(cookies,str(viewS))
    payload = ("javax.faces.partial.ajax=true&javax.faces.source=form%3Aj_idt" + formID
                            + "&javax.faces.partial.execute=form%3Aj_idt" + formID
                            + "&javax.faces.partial.render=form%3Aj_idt" + formID
                            + "&form%3Aj_idt" + formID + "=form%3Aj_idt" + formID
                            + "&form%3Aj_idt" + formID + "_start=" + start
                            + "&form%3Aj_idt" + formID + "_end=" + end
                            + "&form=form"
                            + "&form%3AlargeurDivCenter=1219"
                            + "&form%3Adate_input=" + monday
                            + "&form%3Aweek=" + week_number + "-" + year_number
                            + "&form%3Aj_idt" + formID
                            + "_view=agendaWeek&form%3AoffsetFuseauNavigateur=" + tz
                            + "&form%3Aonglets_activeIndex=0&form%3Aonglets_scrollState=0&form%3Aj_idt236_focus=&form%3Aj_idt236_input=44323"
                            + "&javax.faces.ViewState=" + urllib.parse.quote(viewS))
    # print(payload)
    lenP = str(len(payload)+1)

    conn = http.client.HTTPSConnection("aurion.junia.com")
    headers = {"Cookie": str(cookies),
                "Content-Length": lenP
        }
    conn.request("POST", "/faces/Planning.xhtml",  payload, headers)
    res = conn.getresponse()
    resS = res.status
    resH = res.headers
    resR = res.read()
    print(resS)
    # print(resH)
    print(resR.decode('utf-8'))
    pass

def POSTplanB(cookies):
    GETmain(cookies,baseURL)    
    viewS = ViewState(GETplanning(cookies,baseURL))
    id = 1
    id = str(id)
    payload =("javax.faces.partial.ajax=true&javax.faces.source=form%3Aj_idt117&" +
                "javax.faces.partial.execute=form%3Aj_idt117&javax.faces.partial.render=form%3AmodaleDetail+form%3AconfirmerSuppression&" +
                "javax.faces.behavior.event=eventSelect&javax.faces.partial.event=eventSelect&" +
                "form%3Aj_idt117_selectedEventId=" + id + "&" +
                "form=form&form%3AlargeurDivCenter=1219&form%3Aj_idt117_view=agendaWeek&" +
                "form%3AoffsetFuseauNavigateur=-7200000&form%3Aonglets_activeIndex=0&form%3Aonglets_scrollState=0&form%3Aj_idt236_focus=&" +
                "form%3Aj_idt236_input=44323"
                + "&javax.faces.ViewState=" + urllib.parse.quote(viewS))
    # print(payload)
    lenP = str(len(payload)+1)

    conn = http.client.HTTPSConnection("aurion.junia.com")
    headers = {"Cookie": cookies,
                "Content-Length": lenP
        }
    conn.request("POST", "/faces/Planning.xhtml", payload, headers)
    res = conn.getresponse()
    resS = res.status
    resH = res.headers
    resR = res.read()
    print(resS)
    # print(resH)
    print(resR.decode('utf-8'))
    pass


cookies = Cookies(POSTlogin(username,password))
# viewS = ViewState(GETmain(cookies,baseURL))
# print(cookies, viewS)

POSTplanA(cookies)

