from bs4 import BeautifulSoup


def table(data):         
    # traitement de la table
    soup = BeautifulSoup(data, 'lxml')

    # séparation des notes, dans une liste de liste sous la forme:
    # Date, Code, Nom, Note, Coef
    d = []
    i = 0
    for tr in (soup.select('tr')):
        d.append([]) 
        for sp in (tr.select('span')):
            d[i].append(sp.text)
        i+=1
    
    # transformation du Code en:
    # Annee, Lieu, Prepa, Semestre, Matiere, Type
    for i in range(len(d)):
        d[i][1] = str(d[i][1]).split("_")
        if "CNB1" in d[i][1]:
            d[i][1].remove("CNB1")
        if "CPG1" in d[i][1]:
            d[i][1].remove("CPG1")
    
    final = []
    for i in range(len(d)):
        # print(d[i][1][0])
        if (d[i][1][0] == '2122'):
            final.append(d[i])
        
    # print(final)
    return final