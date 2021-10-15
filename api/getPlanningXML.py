import requests

def getPlanningXML(url ,cookie):
    headers = {"Accept": "application/xml, text/xml, */*; q=0.01"
                ,"Accept-Language": "fr-FR"
                ,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
                ,"Faces-Request": "partial/ajax"
                ,"X-Requested-With": "XMLHttpRequest"
                ,"Origin": "https://aurion.junia.com"
                ,"Connection": "keep-alive"
                ,"Referer": url
                ,"Cookie": cookie
                ,"Sec-Fetch-Dest": "empty"
                ,"Sec-Fetch-Mode": "cors"
                ,"Sec-Fetch-Site": "same-origin"
                ,"Cache-Control": "max-age=0"}
    data = ("javax.faces.partial.ajax=true&javax.faces.source=form%3Aj_idt117&javax.faces.partial.execute=form%3Aj_idt117&javax.faces.partial.render=form%3Aj_idt117&form%3Aj_idt117=form%3Aj_idt117&form%3Aj_idt117_start=1633298400000&form%3Aj_idt117_end=1633816800000&form=form&form%3AlargeurDivCenter=1603&form%3Adate_input=04%2F10%2F2021&form%3Aweek=40-2021&form%3Aj_idt117_view=agendaWeek&form%3AoffsetFuseauNavigateur=-7200000&form%3Aonglets_activeIndex=0&form%3Aonglets_scrollState=0&form%3Aj_idt236_focus=&form%3Aj_idt236_input=44323&javax.faces.ViewState=-3104452961576329710:8474217028661712850")
    
    # print(headers)
    # print(data)

    resp = requests.post(url, headers=headers, data=data)
    return(resp.text)