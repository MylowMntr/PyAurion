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
    
    # for i in range(len(d)):
    #     d[i][2] = str(d[i][2]).split()
        
    # print(d)
    return d