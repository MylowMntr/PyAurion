from TableNotes import table 
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR')
# from getnotes import main
# result = main()
# result = table(result)

resultats = table()
# print(resultats)

def maths(result):
    maths,partiel = [],[]
    for i in range(len(result)):
        if (("MATH1" in result[i][1]) or ("MATH2" in result[i][1]) or ("MATH3" in result[i][1]) or ("MATH4" in result[i][1])): 
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    maths.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
    return maths, partiel

def prog(result):
    prog,partiel,ds = [],[],[]
    for i in range(len(result)):
        if (("PROG1" in result[i][1]) or ("PROG2" in result[i][1])):
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1]) and ("DS" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    prog.append(result[i])
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            if ("DS" in result[i][1]):
                if (result[i][1] != result[i-1][1]):
                    ds.append(result[i])
    return prog, partiel, ds

def web(result):
    web,partiel,ds = [],[],[]
    for i in range(len(result)):
        if ("WEB" in result[i][1]):
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1]) and ("DS" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    web.append(result[i])
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            if ("DS" in result[i][1]):
                if (result[i][1] != result[i-1][1]):
                    ds.append(result[i])
    return web, partiel, ds

def optique(result):
    opt,partiel = [],[]
    for i in range(len(result)):
        if ("OPTIQUE" in result[i][1]) : 
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    opt.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
    return opt, partiel
def electronique(result):
    elec,partiel,tp = [],[],[]
    for i in range(len(result)):
        if ("ELEC" in result[i][1]) : 
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    elec.append(result[i])
            if (("TP1" in result[i][1]) or ("TP2" in result[i][1]) or ("TP3" in result[i][1]) or ("TP4" in result[i][1]) or ("TP5" in result[i][1]) or ("TP6" in result[i][1]) or ("TP7" in result[i][1]) or ("TP8" in result[i][1]) or ("TP9" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    tp.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
    return elec, partiel
def mecanique(result):
    meca,partiel = [],[]
    for i in range(len(result)):
        if ("MECANIQUE" in result[i][1]) : 
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    meca.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
    return meca, partiel

def anglais(result):
    ang = []
    for i in range(len(result)):
        if ("ANGLAIS" in result[i][1]): 
            ang.append(result[i])
    return ang
def comm(result):
    com = []
    for i in range(len(result)):
        if ("COMM" in result[i][1]): 
            com.append(result[i])
    return com
def sport(result):
    spo = []
    for i in range(len(result)):
        if ("SPORT" in result[i][1]): 
            spo.append(result[i])
    return spo
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
def Moyenne(Notes, Coefs):
    for g in range(len(Notes)):
        Notes[g] = Notes[g] * Coefs[g] / sum(Coefs)
    moy = round(sum(Notes),2)
    return moy

def MATHS():
    # print(matiere(maths(resultats)[0]))
    # print(matiere(maths(resultats)[1]))
    note = (Moyenne(matiere(maths(resultats)[0])[0],matiere(maths(resultats)[0])[1]))
    notep = (Moyenne(matiere(maths(resultats)[1])[0],matiere(maths(resultats)[1])[1]))

    note = (note*0.4) + (notep*0.6)
    return(round(note,2))
# MATHS()


def PROG():
    # print(matiere(prog(resultats)[0]))
    # print(matiere(prog(resultats)[1]))
    # print(matiere(prog(resultats)[2]))
    note = (Moyenne(matiere(prog(resultats)[0])[0],matiere(prog(resultats)[0])[1]))
    notep = (Moyenne(matiere(prog(resultats)[1])[0],matiere(prog(resultats)[1])[1]))
    noteds = (Moyenne(matiere(prog(resultats)[2])[0],matiere(prog(resultats)[2])[1]))
    
    
    if (notep == 0):
        note = note*0.4 + noteds*0.6
    if (noteds == 0):
        note = (note*0.4) + (notep*0.6)
    if ((notep == 0) and (noteds == 0)):
        note = note  
    if ((note != 0) and (noteds != 0) and (notep != 0)):
        note = (note*0.4) + (((noteds*0.33)+(notep*0.67))*0.6) 
    return (round(note,2))

def WEB():
    # print(matiere(web(resultats)[0]))
    # print(matiere(web(resultats)[1]))
    # print(matiere(web(resultats)[2]))
    note = (Moyenne(matiere(web(resultats)[0])[0],matiere(web(resultats)[0])[1]))
    notep = (Moyenne(matiere(web(resultats)[1])[0],matiere(web(resultats)[1])[1]))
    noteds = (Moyenne(matiere(web(resultats)[2])[0],matiere(web(resultats)[2])[1]))
    
    
    if (notep == 0):
        note = (note*0.4) + (noteds*0.6)
    if (noteds == 0):
        note = (note*0.4) + (notep*0.6)
    if ((notep == 0) and (noteds == 0)):
        note = note  
    if ((note != 0) and (noteds != 0) and (notep != 0)):
        note = (note*0.4) + (((noteds*0.33)+(notep*0.67))*0.6) 
    return(round(note,2))

def INFO():
    noteprog = PROG()
    noteweb = WEB()
    if (noteprog == 0): note = noteweb
    if (noteweb == 0): note = noteprog
    else:
        note = [noteprog, noteweb]
        coef = [3,2]
        note = Moyenne(note, coef)
    return(round(note,2))
# INFO()    


def PHYSIQUE():
    note = (Moyenne(matiere(optique(resultats)[0])[0],matiere(optique(resultats)[0])[1]))
    notep = (Moyenne(matiere(optique(resultats)[1])[0],matiere(optique(resultats)[1])[1]))
    noteopt = (note*0.4) + (notep*0.6)
    
    note = (Moyenne(matiere(electronique(resultats)[0])[0],matiere(electronique(resultats)[0])[1]))
    notep = (Moyenne(matiere(electronique(resultats)[1])[0],matiere(electronique(resultats)[1])[1]))
    noteelec = (note*0.4) + (notep*0.6)
    
    if (noteopt == 0): note = noteelec
    if (noteelec == 0): note = noteopt
    else:
        note = [noteopt, noteelec]
        coef = [2,3]
        note = Moyenne(note, coef)
    return(round(note,2))
# PHYSIQUE()

def DEV():
    noteang = (Moyenne(matiere(anglais(resultats))[0],matiere(anglais(resultats))[1]))
    notecomm = (Moyenne(matiere(comm(resultats))[0],matiere(comm(resultats))[1]))
    notespo = (Moyenne(matiere(sport(resultats))[0],matiere(sport(resultats))[1]))
    note = [noteang, notecomm, notespo]
    coef = [2,2,2]
    note = Moyenne(note, coef)
    return(round(note,2))
# DEV()