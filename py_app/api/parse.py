from pathlib import Path
import datetime
import json

""" Transforme les dictionnaire python en un fichier ics
Format corespondance :

BEGIN:VEVENT

UID - "id": 
SUMMARY - "title": 
DTSTART - "start": 
DTEND - "end": 
CATEGORIES - "className"

"allDay":false,
"editable":true,

END:VEVENT 
"""


def main(calendrier):
    calendrier = json.loads(calendrier)
    false = False
    true = True
    downloads_path = str(Path.home() / "Downloads/planning.ics")
    sortie = open(downloads_path, "w", encoding="utf-8")
    sortie.write("BEGIN:VCALENDAR\nVERSION:2.0\n")

    #data=re.sub(r'\\(.)', r'\1', data)
    #title = re.findall('"title": "(.+?)",', full)

    id = []
    title = []
    start = []
    end = []
    className = []

    for dictionnaire in calendrier:
        id.append(dictionnaire.get("id"))
        title.append(dictionnaire.get("title"))
        start.append(dictionnaire.get("start"))
        end.append(dictionnaire.get("end"))
        className.append(dictionnaire.get("className", "Type inconnue"))

        # DTSTART:2022-03-21T13:30:00+0100  ---> 19970714T170000Z
        #str=datetime.strptime(start[i], '%Y-%m-%dT%H:%M:%S%z').strftime("yyyyMMdd'T'HHmmss'Z'")
    for i in range(len(calendrier)):  # Pour chaque évènement
        dateS = datetime.datetime.strptime(start[i], '%Y-%m-%dT%H:%M:%S%z')
        debut = datetime.datetime.strftime(dateS, "%Y%m%dT%H%M%S")
        dateF = datetime.datetime.strptime(end[i], '%Y-%m-%dT%H:%M:%S%z')
        fin = datetime.datetime.strftime(dateF, "%Y%m%dT%H%M%S")
        title[i] = title[i].replace('\n', '\\n')

        sortie.write("BEGIN:VEVENT\nUID:"+id[i] +
                     "\nSUMMARY:"+title[i] +
                     "\nDTSTART:"+debut+"\nDTEND:"+fin +
                     "\nDESCRIPTION:"+className[i] +
                     "\nEND:VEVENT\n")

    sortie.write("END:VCALENDAR")
    sortie.close()

    fi = "Fichier \"planning.ics\" créer dans les téléchargements"
    return fi
