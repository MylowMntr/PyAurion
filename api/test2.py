def getGrades(self):
    cookie = PreferenceUtils.getSessionId()
    aurionResponse = AurionResponse()
    data = None
    res = None

    #accueil
    data = getHomePage(cookie)

    #postState
    defaultFields = "javax.faces.partial.ajax=true&javax.faces.source=form%3Aj_idt52&" + "javax.faces.partial.execute=form%3Aj_idt52&javax.faces.partial.render=form%3Asidebar&" + "form%3Aj_idt52=form%3Aj_idt52&webscolaapp.Sidebar.ID_SUBMENU=submenu_44413&form=form&" + "form%3AlargeurDivCenter=1219&form%3Asauvegarde=&form%3Aj_idt772_focus=&form%3Aj_idt772_input=44323"
    fields = {}
    fieldsArray = defaultFields.split("&")
    i = 0
    while i < len(fieldsArray):
        keyVal = fieldsArray[i].split("=")
        if len(keyVal) == 2:
            fields.update({keyVal[0]: keyVal[1]})
        else:
            fields.update({keyVal[0]: ""})
        i += 1

    request = aurionService.postMainMenuPage(cookie, data.viewState, fields)
    try:
        res = request.execute()
        if res.isSuccessful():
            body = res.body().string()

            from_keyword_conflict = ""
            to = "Mes notes</span>"
            menuid = body[body.find(to) - 300:body.find(to)]
            from_keyword_conflict = "form:sidebar_menuid':'"
            to = "'})"
            menuid = menuid[menuid.find(from_keyword_conflict) + len(from_keyword_conflict):menuid.find(to)]

            defaultFields = "form=form&form%3AlargeurDivCenter=1219&form%3Asauvegarde=&" + "form%3Aj_idt772_focus=&form%3Aj_idt772_input=44323&" + "form%3Asidebar=form%3Asidebar&form%3Asidebar_menuid=" + menuid
            fields.clear()
            fieldsArray = defaultFields.split("&")
            i = 0
            while i < len(fieldsArray):
                keyVal = fieldsArray[i].split("=")
                if len(keyVal) == 2:
                    fields.update({keyVal[0]: keyVal[1]})
                else:
                    fields.update({keyVal[0]: ""})
                i += 1
            request = aurionService.postMainMenuPage(cookie, data.viewState, fields)

            res = request.execute()
            if res.code() == 302:
                #body = res.headers().toString()
                request = aurionService.getGradesHtml(cookie)
                res = request.execute()
                if res.isSuccessful():
                    body = res.body().string()

                    from_keyword_conflict = "javax.faces.ViewState:0\" value=\""
                    to = "\" autocomplete=\"off\" />"

                    data.viewState = body[body.find(from_keyword_conflict) + len(from_keyword_conflict):body.find(to)]
                    start = 0
                    rows = 10000
                    defaultFields = "javax.faces.partial.ajax=true&javax.faces.source=form%3Aj_idt181&" + "javax.faces.partial.execute=form%3Aj_idt181&javax.faces.partial.render=form%3Aj_idt181&" + "form%3Aj_idt181=form%3Aj_idt181&form%3Aj_idt181_pagination=true&" + "form%3Aj_idt181_first=" + start + "&form%3Aj_idt181_rows=" + rows + "&form%3Aj_idt181_skipChildren=true&form%3Aj_idt181_encodeFeature=true&" + "form=form&form%3AlargeurDivCenter=835&form%3AmessagesRubriqueInaccessible=&form%3Asearch-texte=&" + "form%3Asearch-texte-avancer=&form%3Ainput-expression-exacte=&form%3Ainput-un-des-mots=&" + "form%3Ainput-aucun-des-mots=&form%3Ainput-nombre-debut=&form%3Ainput-nombre-fin=&" + "form%3AcalendarDebut_input=&form%3AcalendarFin_input=&form%3Aj_idt181_reflowDD=0_0&" + "form%3Aj_idt181%3Aj_idt186%3Afilter=&form%3Aj_idt181%3Aj_idt188%3Afilter=&" + "form%3Aj_idt181%3Aj_idt190%3Afilter=&form%3Aj_idt181%3Aj_idt192%3Afilter=&" + "form%3Aj_idt181%3Aj_idt194%3Afilter=&form%3Aj_idt181%3Aj_idt196%3Afilter=&form%3Aj_idt254_focus=&" + "form%3Aj_idt254_input=44323"
                    fields.clear()
                    fieldsArray = defaultFields.split("&")
                    i = 0
                    while i < len(fieldsArray):
                        keyVal = fieldsArray[i].split("=")
                        if len(keyVal) == 2:
                            fields.update({keyVal[0]: keyVal[1]})
                        i += 1

                    request = aurionService.postGrades(cookie, data.viewState, fields)
                    res = request.execute()

                    if res.isSuccessful():
                        body = res.body().string()
                        aurionResponse.status = AurionResponse.SUCCESS
                        aurionResponse.body = body

        else:
            aurionResponse.status = AurionResponse.FAILURE
            aurionResponse.message = "Authentication failed"
    except IOException as e:
        e.printStackTrace()
        aurionResponse.status = AurionResponse.FAILURE
        aurionResponse.message = "Server couldn't be reached : check your connection"

    return aurionResponse
