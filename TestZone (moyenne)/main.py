from TableNotes import table
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

    note = [noteopt, noteelec, TPelec]
    coef = [2,3,3]
    final = MoyenneC(note, coef)
    return final


def mecanique(result):
    meca,partiel,coef = [],[],3
    for i in range(len(result)):
        if ("MECANIQUE" in result[i][1]) : 
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    meca.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
    return meca, partiel, coef

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
    # result = getnotes.main(username,password)
    # # print(result)
    result = '''
    <tr data-ri="0" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">07/01/2022</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_WEB_P1</span></td><td role="gridcell" class=""><span class="preformatted ">Partiel de Technologies Web</span></td><td role="gridcell" class=""><span class="preformatted "> 16.60</span></td><td role="gridcell" class=""><span class="preformatted ">24</span></td><td role="gridcell" class=""></td></tr><tr data-ri="1" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">06/01/2022</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_PROG1_P1</span></td><td role="gridcell" class=""><span class="preformatted ">Epreuve de Partiel</span></td><td role="gridcell" class=""><span class="preformatted "> 16.20</span></td><td role="gridcell" class=""><span class="preformatted ">40</span></td><td role="gridcell" class=""></td></tr><tr data-ri="2" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">05/01/2022</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_ELEC_P1</span></td><td role="gridcell" class=""><span class="preformatted ">Epreuve de Partiel</span></td><td role="gridcell" class=""><span class="preformatted ">  4.00</span></td><td role="gridcell" class=""><span class="preformatted ">60</span></td><td role="gridcell" class=""></td></tr><tr data-ri="3" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">03/01/2022</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_P1</span></td><td role="gridcell" class=""><span class="preformatted ">Partiel de Mathématiques</span></td><td role="gridcell" class=""><span class="preformatted ">  4.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="4" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">15/12/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_MATH_TP6_1</span></td><td role="gridcell" class=""><span class="preformatted ">Evaluation du TP6</span></td><td role="gridcell" class=""><span class="preformatted "> 17.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="5" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">10/12/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_CC5</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu de Mathématiques n°5</span></td><td role="gridcell" class=""><span class="preformatted ">  6.40</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="6" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">10/12/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_WEB_CC2</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu de Technologies Web n°2</span></td><td role="gridcell" class=""><span class="preformatted "> 12.67</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="7" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">09/12/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_ELEC_DS</span></td><td role="gridcell" class=""><span class="preformatted ">Devoir Surveillé d'Électronique</span></td><td role="gridcell" class=""><span class="preformatted ">  7.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="8" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">08/12/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_ELEC_TP4_1</span></td><td role="gridcell" class=""><span class="preformatted ">Evaluation du TP4</span></td><td role="gridcell" class=""><span class="preformatted "> 19.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="9" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">06/12/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_ANGLAIS_1_NOTE</span></td><td role="gridcell" class=""><span class="preformatted ">Moyenne d'Anglais (groupe 1)</span></td><td role="gridcell" class=""><span class="preformatted "> 14.04</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="10" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">06/12/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_SPORT_T1</span></td><td role="gridcell" class=""><span class="preformatted ">Note de Sport Tiers 1</span></td><td role="gridcell" class=""><span class="preformatted "> 15.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="11" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">06/12/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_WEB_PROJ</span></td><td role="gridcell" class=""><span class="preformatted ">Projet de Technologies Web</span></td><td role="gridcell" class=""><span class="preformatted "> 15.00</span></td><td role="gridcell" class=""><span class="preformatted ">100</span></td><td role="gridcell" class=""></td></tr><tr data-ri="12" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">29/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_INFO_PRAT_TP_C_Q1</span></td><td role="gridcell" class=""><span class="preformatted ">Travaux pratiques de C</span></td><td role="gridcell" class=""><span class="preformatted "> 17.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="13" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">26/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_CC4</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu de Mathématiques n°4</span></td><td role="gridcell" class=""><span class="preformatted ">  7.10</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="14" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">26/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_PROG1_CC2</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu n°2</span></td><td role="gridcell" class=""><span class="preformatted "> 13.75</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="15" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">24/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_IE3</span></td><td role="gridcell" class=""><span class="preformatted ">Interrogation de cours n°3</span></td><td role="gridcell" class=""><span class="preformatted ">  0.00</span></td><td role="gridcell" class=""><span class="preformatted ">0,33</span></td><td role="gridcell" class=""></td></tr><tr data-ri="16" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">24/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_IE3</span></td><td role="gridcell" class=""><span class="preformatted ">Interrogation de cours n°3</span></td><td role="gridcell" class=""><span class="preformatted ">  0.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="17" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">24/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_ELEC_TP3_1</span></td><td role="gridcell" class=""><span class="preformatted ">Evaluation du TP3</span></td><td role="gridcell" class=""><span class="preformatted "> 14.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="18" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">19/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_WEB_DS</span></td><td role="gridcell" class=""><span class="preformatted ">DS Technologies Web</span></td><td role="gridcell" class=""><span class="preformatted "> 15.12</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="19" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">17/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_IE2</span></td><td role="gridcell" class=""><span class="preformatted ">Interrogation de cours n°2</span></td><td role="gridcell" class=""><span class="preformatted ">  8.00</span></td><td role="gridcell" class=""><span class="preformatted ">0,33</span></td><td role="gridcell" class=""></td></tr><tr data-ri="20" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">17/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_IE2</span></td><td role="gridcell" class=""><span class="preformatted ">Interrogation de cours n°2</span></td><td role="gridcell" class=""><span class="preformatted ">  8.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="21" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">17/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_MATH_TP4_1</span></td><td role="gridcell" class=""><span class="preformatted ">Evaluation du TP4</span></td><td role="gridcell" class=""><span class="preformatted "> 17.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="22" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">13/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH1_P2</span></td><td role="gridcell" class=""><span class="preformatted ">Examen de Mathématiques (seconde session)</span></td><td role="gridcell" class=""><span class="preformatted "> 11.25</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="23" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">12/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_ELEC_CC</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu d'Electronique</span></td><td role="gridcell" class=""><span class="preformatted "> 11.50</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="24" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">12/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_CC3</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu de Mathématiques n°3</span></td><td role="gridcell" class=""><span class="preformatted "> 12.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="25" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">10/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_IE1</span></td><td role="gridcell" class=""><span class="preformatted ">Interrogation de cours n°1</span></td><td role="gridcell" class=""><span class="preformatted "> 15.00</span></td><td role="gridcell" class=""><span class="preformatted ">0,33</span></td><td role="gridcell" class=""></td></tr><tr data-ri="26" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">10/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH2_IE1</span></td><td role="gridcell" class=""><span class="preformatted ">Interrogation de cours n°1</span></td><td role="gridcell" class=""><span class="preformatted "> 15.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="27" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">10/11/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_ELEC_TP2_1</span></td><td role="gridcell" class=""><span class="preformatted ">Evaluation du TP2</span></td><td role="gridcell" class=""><span class="preformatted "> 10.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="28" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">22/10/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_PROG1_DS</span></td><td role="gridcell" class=""><span class="preformatted ">Devoir surveillé de Programmation</span></td><td role="gridcell" class=""><span class="preformatted "> 17.20</span></td><td role="gridcell" class=""><span class="preformatted ">20</span></td><td role="gridcell" class=""></td></tr><tr data-ri="29" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">20/10/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_MATH_TP3_1</span></td><td role="gridcell" class=""><span class="preformatted ">Evaluation du TP3</span></td><td role="gridcell" class=""><span class="preformatted "> 18.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="30" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">15/10/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH1_P1</span></td><td role="gridcell" class=""><span class="preformatted ">Partiel de Mathématiques</span></td><td role="gridcell" class=""><span class="preformatted ">  3.50</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="31" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">15/10/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH1_P1</span></td><td role="gridcell" class=""><span class="preformatted ">Partiel de Mathématiques</span></td><td role="gridcell" class=""><span class="preformatted ">  3.50</span></td><td role="gridcell" class=""><span class="preformatted ">2</span></td><td role="gridcell" class=""></td></tr><tr data-ri="32" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">13/10/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_ELEC_TP1_1</span></td><td role="gridcell" class=""><span class="preformatted ">Evaluation du TP1</span></td><td role="gridcell" class=""><span class="preformatted "> 13.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="33" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">08/10/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_OPTIQUE_P1</span></td><td role="gridcell" class=""><span class="preformatted ">Partiel d'Optique Géométrique</span></td><td role="gridcell" class=""><span class="preformatted ">  9.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="34" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">04/10/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_COMM_ORAL</span></td><td role="gridcell" class=""><span class="preformatted ">Exposé oral</span></td><td role="gridcell" class=""><span class="preformatted "> 17.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="35" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">01/10/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH1_CC2</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu de Mathématiques n°2</span></td><td role="gridcell" class=""><span class="preformatted "> 11.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="36" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">01/10/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_WEB_CC</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu de Technologies Web n°1</span></td><td role="gridcell" class=""><span class="preformatted "> 13.94</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="37" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">24/09/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_S1_PROG1_CC1</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu de Programmation</span></td><td role="gridcell" class=""><span class="preformatted "> 11.67</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="38" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">17/09/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH1_CC1</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu de Mathématiques n°1</span></td><td role="gridcell" class=""><span class="preformatted ">  9.80</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="39" class="ui-widget-content ui-datatable-odd CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">17/09/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_OPTIQUE_CC</span></td><td role="gridcell" class=""><span class="preformatted ">Contrôle Continu d'Optique Géométrique</span></td><td role="gridcell" class=""><span class="preformatted "> 13.00</span></td><td role="gridcell" class=""><span class="preformatted ">1</span></td><td role="gridcell" class=""></td></tr><tr data-ri="40" class="ui-widget-content ui-datatable-even CursorInitial" role="row"><td role="gridcell" class="TexAlLeft"><span class="preformatted ">10/09/2021</span></td><td role="gridcell" class=""><span class="preformatted ">2122_ISEN_CIR1_CNB1_S1_MATH1_CC0</span></td><td role="gridcell" class=""><span class="preformatted ">QCM mathématiques de rentrée</span></td><td role="gridcell" class=""><span class="preformatted "> 14.50</span></td><td role="gridcell" class=""></td><td role="gridcell" class=""></td></tr>
    '''
    
    resultats = table(result)  #Liste de liste de note sous forme ['07/01/2022', ['2122', 'ISEN', 'CIR1', 'S1', 'WEB', 'P1'], 'Partiel de Technologies Web', ' 16.60', '24']
    # print(resultats)
    print(MATHS(resultats),PHYSIQUE(resultats),INFO(resultats),DEV(resultats))
    
main("fds", "dsf")