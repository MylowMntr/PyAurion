from . import TableNotes, getnotes
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR')


def maths(result):
    maths,partiel,coef,TP,IE,sumIE = [],[],3,[],[],0
    # print(result)
    for i in range(len(result)):
        if (("MATH" in result[i][1][4])):
            # print(result[i][1])
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            elif (("TP" in result[i][1][5])):
                if (result[i][1] != result[i-1][1]):
                    TP.append(result[i])
            elif (("IE" in result[i][1][5])):
                if (result[i][1] != result[i-1][1]):
                    IE.append(result[i])
                    sumIE += float(locale.atof(result[i][3]))
            else:
                if (result[i][1] != result[i-1][1]):
                    maths.append(result[i])
    # print(IE,"\n",partiel,"\n",TP,"\n",maths) 

    IE = (Moyenne(matiere(IE)[0]))
    if (IE == 21):
        return "ERREUR maths IE"
    maths = matiere(maths)
    maths[0].append(IE)
    note = Moyenne(maths[0])
    # print(note)
    notep = Moyenne(matiere(partiel)[0])
    if (notep == 21):
        return "ERREUR maths Partiel"
    # print(notep)

    notetp = Moyenne(matiere(TP)[0])
    # print(notetp)
    if (notetp == 21):
        return "ERREUR maths TP"

    note = (note*0.4) + (notep*0.6)
    # print(note)
    notes = [note,notetp]
    coefs = [12,4]
    final = MoyenneC(notes, coefs)
    # print(final)
    # Maths coef 12 + TP coef 4
    return final

def prog(result):
    prog,partiel,ds,tp,coef = [],[],[],[],3
    for i in range(len(result)):
        if (("PROG1" in result[i][1]) or ("PROG2" in result[i][1])):
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1]) and ("DS" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    prog.append(result[i])
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            if (("TP1" in result[i][1]) or ("TP2" in result[i][1]) or ("TP3" in result[i][1]) or ("TP4" in result[i][1]) or ("TP5" in result[i][1]) or ("TP6" in result[i][1]) or ("TP7" in result[i][1]) or ("TP8" in result[i][1]) or ("TP9" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    tp.append(result[i])
            if ("DS" in result[i][1]):
                if (result[i][1] != result[i-1][1]):
                    ds.append(result[i])
    return prog, partiel, ds, coef

def info(result):
    tp,coef = [],3
    for i in range(len(result)):
        if ("INFO" in result[i][1]):
            if ("TP" in result[i][1]):
                if (result[i][1] != result[i-1][1]):
                    tp.append(result[i])
    return tp,coef

def web(result):
    web,partiel,ds,tp,coef = [],[],[],[],2
    for i in range(len(result)):
        if ("WEB" in result[i][1]):
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1]) and ("DS" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    web.append(result[i])
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            if (("TP1" in result[i][1]) or ("TP2" in result[i][1]) or ("TP3" in result[i][1]) or ("TP4" in result[i][1]) or ("TP5" in result[i][1]) or ("TP6" in result[i][1]) or ("TP7" in result[i][1]) or ("TP8" in result[i][1]) or ("TP9" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    tp.append(result[i])
            if ("DS" in result[i][1]):
                if (result[i][1] != result[i-1][1]):
                    ds.append(result[i])
    return web, partiel, ds, coef

def physique(result):
    elec,partiel,TP,coef = [],[],[],3
    for i in range(len(result)):
        if ("ELEC" in result[i][1]) : 
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            elif (("TP" in result[i][1][5])) :
                if (result[i][1] != result[i-1][1]):
                    TP.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    elec.append(result[i])
                    
    note = Moyenne(matiere(elec)[0])
    if (note == 21):
        return "ERREUR elec CC"
    # print(note)
    notep = Moyenne(matiere(partiel)[0])
    if (notep == 21):
        return "ERREUR elec partiel"
    # print(notep)
    TPelec = Moyenne(matiere(TP)[0])
    if (TPelec == 21):
        return "ERREUR maths TP"
    # print(notetp)
    noteelec = (note*0.4) + (notep*0.6)
    # print(noteelec,TPelec)


    opt,partiel,coef = [],[],2
    for i in range(len(result)):
        if ("OPTIQUE" in result[i][1]) : 
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    opt.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
                    

    note = Moyenne(matiere(opt)[0])
    if (note == 21):
        return "ERREUR optique CC"
    notep = Moyenne(matiere(partiel)[0])
    if (notep == 21):
        return "ERREUR optique Partiel"
    # print(note,notep)
    noteopt = (note*0.4) + (notep*0.6)
    # print(noteopt)

    meca,partiel = [],[]
    for i in range(len(result)):
        if ("MECA" in result[i][1]) : 
            # print(result[i])
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    meca.append(result[i])
            # else:
            #     if (result[i][1] != result[i-1][1]):
            #         partiel.append(result[i])
    # print(meca)
    note = Moyenne(matiere(meca)[0])
    # print(note)
    if (note == 21):
        return "ERREUR meca CC"
    # notep = Moyenne(matiere(partiel)[0])
    # if (notep == 21):
    #     return "ERREUR meca Partiel"
    notemeca = note
    
    
    note = [noteopt, noteelec, TPelec, notemeca]
    print(note)
    coef = [2,3,3,3]
    final = MoyenneC(note, coef)
    return final

def anglais(result):
    ang,coef = [],2
    for i in range(len(result)):
        if ("ANGLAIS" in result[i][1]): 
            ang.append(result[i])
    return ang,coef
def comm(result):
    com,coef = [],2
    for i in range(len(result)):
        if ("COMM" in result[i][1]): 
            com.append(result[i])
    return com,coef
def sport(result):
    spo, coef = [],2
    for i in range(len(result)):
        if ("SPORT" in result[i][1]): 
            spo.append(result[i])
    return spo,coef



# Calcul par rapport au coef des notes de result
def matiere(result):
    Notes = []
    Coefs = []
    for i in range (len(result)):
        # print(result[i])
        if (len(result[i]) == 5):
            Notes.append(float(locale.atof(result[i][3])))
            Coefs.append(float(locale.atof(result[i][4])))
    return Notes,Coefs
    
# moyenne a partir d'une liste de note du module
def Moyenne(Notes):
    if (Notes != []):
        moy = sum(Notes)/len(Notes)
    else: 
        moy = 21
    return moy

def MoyenneC(Notes, Coefs):
    try:
        moy = sum(Notes[g] * Coefs[g] / sum(Coefs) for g in range(len(Notes)))
        moy = (round(moy,2))
        return moy
    except:
        return "ERREUR calcul moyenne"


def MATHS(resultats):
    final = maths(resultats)
    return(final)
# MATHS()


def PROG(resultats):
    # print(matiere(prog(resultats)[0]))
    # print(matiere(prog(resultats)[1]))
    # print(matiere(prog(resultats)[2]))
    note = (Moyenne(matiere(prog(resultats)[0])[0]))
    if (note == 21):
        return "ERREUR prog CC"
    notep = (Moyenne(matiere(prog(resultats)[1])[0]))
    if (notep == 21):
        return "ERREUR prog partiel"
    noteds = (Moyenne(matiere(prog(resultats)[2])[0]))
    if (noteds == 21):
        return "ERREUR optique DS"
    
    
    if (notep == 0):
        note = note*0.4 + noteds*0.6
    if (noteds == 0):
        note = (note*0.4) + (notep*0.6)
    if ((notep == 0) and (noteds == 0)):
        note = note  
    if ((note != 0) and (noteds != 0) and (notep != 0)):
        note = (note*0.4) + (((noteds*0.33)+(notep*0.67))*0.6) 
    final = (round(note,2))
    return final

def WEB(resultats):
    # print(matiere(web(resultats)[0]))
    # print(matiere(web(resultats)[1]))
    # print(matiere(web(resultats)[2]))
    note = (Moyenne(matiere(web(resultats)[0])[0]))
    if (note == 21):
        return "ERREUR web CC"
    notep = (Moyenne(matiere(web(resultats)[1])[0]))
    if (notep == 21):
        return "ERREUR web partiel"
    noteds = (Moyenne(matiere(web(resultats)[2])[0]))
    if (noteds == 21):
        return "ERREUR web DS"
    
    
    if (notep == 0):
        note = (note*0.4) + (noteds*0.6)
    if (noteds == 0):
        note = (note*0.4) + (notep*0.6)
    if ((notep == 0) and (noteds == 0)):
        note = note  
    if ((note != 0) and (noteds != 0) and (notep != 0)):
        note = (note*0.4) + (((noteds*0.33)+(notep*0.67))*0.6) 
    final = (round(note,2))
    return final

def INFO(resultats):
    noteprog = PROG(resultats)
    noteweb = WEB(resultats)
    notetp = (Moyenne(matiere(info(resultats)[0])[0]))
    if (noteprog == 0): note = noteweb
    if (noteweb == 0): note = noteprog
    else:
        note = [noteprog, noteweb, notetp]
        coef = [3,2,3]
        note = MoyenneC(note, coef)
    if (type(note) == float) :
        return note
    else:
        return "ERREUR calcul info"
# INFO()    


def PHYSIQUE(resultats):
    final = physique(resultats)
    return final
# PHYSIQUE()

def DEV(resultats):
    noteang = (Moyenne(matiere(anglais(resultats)[0])[0]))
    if (noteang == 21):
        return "ERREUR anglais"
    notecomm = (Moyenne(matiere(comm(resultats)[0])[0]))
    if (notecomm == 21):
        return "ERREUR Comm"
    notespo = (Moyenne(matiere(sport(resultats)[0])[0]))
    if (notespo == 21):
        return "ERREUR sport"
    note = [noteang, notecomm, notespo]
    coef = [2,2,2]
    final = MoyenneC(note, coef)
    return final
# DEV()


def main(username,password):
    result = getnotes.main(username,password)
    # print(result)
    resultats = TableNotes.table(result)  #Liste de liste de note sous forme ['07/01/2022', ['2122', 'ISEN', 'CIR1', 'S1', 'WEB', 'P1'], 'Partiel de Technologies Web', ' 16.60', '24']
    # print(resultats)
    
    return MATHS(resultats),PHYSIQUE(resultats),INFO(resultats),DEV(resultats)