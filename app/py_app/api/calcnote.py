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
    web,partiel = [],[]
    for i in range(len(result)):
        if ("WEB" in result[i][1]):
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    web.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
    return web, partiel


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
    print(note)
MATHS()

def PROG():
    print(matiere(prog(resultats)[0]))
    print(matiere(prog(resultats)[1]))
    print(matiere(prog(resultats)[2]))
    note = (Moyenne(matiere(prog(resultats)[0])[0],matiere(prog(resultats)[0])[1]))
    notep = (Moyenne(matiere(prog(resultats)[1])[0],matiere(prog(resultats)[1])[1]))
    noteds = (Moyenne(matiere(prog(resultats)[2])[0],matiere(prog(resultats)[2])[1]))

    note = (note*0.4) + ((noteds*0.33+notep*0.67)*0.6)
    print(note)
PROG()