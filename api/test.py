import datetime


res = None
aurionResponse = AurionResponse()
data = None
df = SimpleDateFormat("dd/MM/yyyy", Locale.FRANCE)
print(df)
now = datetime.datetime().getTimeInMillis()
offset = int((weekIndex - datetime.datetime().get(Calendar.WEEK_OF_YEAR))) * 7 * 24 * 60 * 60 * 1000
start = (now - (now + 3 * 24 * 60 * 60 * 1000) % (7*24*60*60*1000)) + offset
end = start + (6*24*60*60*1000)
   #long end = (6*24*60*60*1000 + Calendar.getInstance().getTime().getTime() - 1 - 3*24*60*60*1000 - Calendar.getInstance().getTime().getTime() % (604_800_000))
    #      + weekIndex * 7 * 24 * 60 * 60 * 1000

defaultFields = None
fields = {}
fieldsArray = []

    #accueil
data = getHomePage(connCookie)

    #postState
defaultFields = "form=form&form%3AlargeurDivCenter=835&form%3Asauvegarde=&form%3Aj_idt772_focus=&form%3Aj_idt772_input=44323&form%3Asidebar=form%3Asidebar&" + "form%3Asidebar_menuid=" + data.schoolingMenuId

        res = request.execute()
        if res.code() == 302:
            data = getPlanningData(connCookie)
            defaultFields = "javax.faces.partial.ajax=true" + "&javax.faces.source=form%3Aj_idt" + data.formId + "&javax.faces.partial.execute=form%3Aj_idt" + data.formId + "&javax.faces.partial.render=form%3Aj_idt" + data.formId + "&form%3Aj_idt" + data.formId + "=form%3Aj_idt" + data.formId + "&form%3Aj_idt" + data.formId + "_start=" + start + "&form%3Aj_idt" + data.formId + "_end=" + end + "&form=form" + "&form%3Adate_input=" + df.format(start).replace("/", "%2F") + "&form%3Aweek=" + weekIndex + "-" + datetime.datetime().year
            fields.clear()
            fieldsArray = defaultFields.split("&")
            i = 0
            while i < len(fieldsArray):
                keyVal = fieldsArray[i].split("=")
                if len(keyVal) == 2:
                    fields.update({keyVal[0]: keyVal[1]})
                i += 1
            request = aurionService.postPlanningPage(connCookie, data.viewState, fields)

            body = None
            res = request.execute()
            if res.isSuccessful():
                body = res.body().string()
                aurionResponse.status = AurionResponse.SUCCESS
                aurionResponse.body = body
        else:
            aurionResponse.status = AurionResponse.FAILURE
            aurionResponse.message = "Authentication failed"
