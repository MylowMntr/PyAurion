from . import TableNotes, getnotes
# import TableNotes, getnotes
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR')

class UE:
    def __init__(self):
        self.cours = []
        
    def moyenne(self):
        TableMoyenne = []
        TableCoef = []
        for i in self.cours:
            TableMoyenne.append(i.moyenne())
        for i in self.cours:
            TableCoef.append(i.coef)
        # print(TableMoyenne,TableCoef)
        moy = sum(TableMoyenne[g] * TableCoef[g] / sum(TableCoef) for g in range(len(TableMoyenne)))
        moy = (round(moy,2))
        return moy

class cours:
    def __init__(self,coef):
        self.coef = coef
        self.Note = []
        self.Partiel = []
        self.DS = []
        self.NbNote = 0
        
    def ajouter(self,new):
        self.NbNote += 1
        self.Note.append(new)
    def ajouterP(self,new):
        self.NbNote += 1
        self.Partiel.append(new)
    def ajouterD(self,new):
        self.NbNote += 1
        self.DS.append(new)
    
    def moyenne(self):
        somme,sommeP,sommeD = 0,0,0
        if (self.Partiel != []):
            if (self.DS != []):
                for i in self.Note:
                    somme += i
                for i in self.Partiel:
                    sommeP += i
                for i in self.DS:
                    sommeD += i
                somme = somme/len(self.Note)
                sommeP = sommeP/len(self.Partiel)
                sommeD = sommeD/len(self.DS)    
                return somme*0.4 + (sommeD*0.33 + sommeP*0.67)*0.6
            
            for i in self.Note:
                somme += i
            for i in self.Partiel:
                sommeP += i
            somme = somme/len(self.Note)
            sommeP = sommeP/len(self.Partiel)    
            return somme*0.4 + sommeP*0.6
        if (self.DS != []):
            if (self.Partiel != []):
                for i in self.Note:
                    somme += i
                for i in self.Partiel:
                    sommeP += i
                for i in self.DS:
                    sommeD += i
                somme = somme/len(self.Note)
                sommeP = sommeP/len(self.Partiel)
                sommeD = sommeD/len(self.DS)    
                return somme*0.4 + (sommeD*0.33 + sommeP*0.67)*0.6
            
            for i in self.Note:
                somme += i
            for i in self.DS:
                sommeD += i
            somme = somme/len(self.Note)
            sommeD = sommeD/len(self.DS)    
            return somme*0.4 + sommeD*0.6
        
        for i in self.Note:
            somme += i
        return somme/self.NbNote
    
    
def rangement(result):
    MathM1 = cours(3)
    MathM2 = cours(3)
    MathM3 = cours(3)
    MathM4 = cours(3)
    MathTpS1 = cours(2)
    MathTpS2 = cours(2)
    Maths = UE()
    Maths.cours.extend((MathM1,MathM2,MathM3,MathM4,MathTpS1,MathTpS2))
    
    Optique = cours(2)
    Elec = cours(3)
    ElecTP = cours(3)
    Meca = cours(3)
    # Thermo = cours(1)
    Physique = UE()
    Physique.cours.extend((Optique,Elec,ElecTP,Meca))
    
    Prog1 = cours(3)
    ProgTPS1 = cours(3)
    WebS1 = cours(2)
    Prog2 = cours(2)
    # ProgTPS2 = cours(2)
    WebS2 = cours(2)
    Arduino = cours(2)
    # Projet = cours(3)
    Info = UE()
    # Info.cours.extend((Prog1,ProgTPS1,WebS1,Prog2,ProgTPS2,WebS2,Arduino,Projet))
    Info.cours.extend((Prog1,ProgTPS1,WebS1,Prog2,WebS2,Arduino))
    
    Anglais1 = cours(2)
    Anglais2 = cours(2)
    CR = cours(2)
    Epistemo = cours(2)
    Sport1 = cours(2)
    Sport2 = cours(2)
    Dev = UE()
    Dev.cours.extend((Anglais1, CR, Sport1))
    
    for i in range(len(result)):
        if (("MATH" in result[i][1][4]) or ("MATHS" in result[i][1])):
            if ("MATH1" in  result[i][1]):
                if ("P" in  result[i][1][5]):
                    MathM1.ajouterP(float(locale.atof(result[i][3])))
                else:
                    MathM1.ajouter(float(locale.atof(result[i][3])))
            if ("MATH2" in  result[i][1]):
                if ("P" in  result[i][1][5]):
                    MathM2.ajouterP(float(locale.atof(result[i][3])))
                else:
                    MathM2.ajouter(float(locale.atof(result[i][3]))) 
            if ("MATH3" in  result[i][1]):
                if ("P" in  result[i][1][5]):
                    MathM3.ajouterP(float(locale.atof(result[i][3])))
                else:
                    MathM3.ajouter(float(locale.atof(result[i][3]))) 
            if ("MATH4" in  result[i][1]):
                if ("P" in  result[i][1][5]):
                    MathM4.ajouterP(float(locale.atof(result[i][3])))
                else:
                    MathM4.ajouter(float(locale.atof(result[i][3]))) 
            
            if ("TP" in result[i][1][5]):
                if ("S1" in result[i][1][3]):
                    MathTpS1.ajouter(float(locale.atof(result[i][3])))
                if ("S2" in result[i][1][3]):
                    MathTpS2.ajouter(float(locale.atof(result[i][3])))
        if (("ELEC" in result[i][1][4]) or ("OPTIQUE" in result[i][1]) or ("MECA" in result[i][1])):
            # print(result[i][1])
            if ("ELEC" in  result[i][1]):
                if ("TP" in result[i][1][5]):
                    ElecTP.ajouter(float(locale.atof(result[i][3])))
                if ("P" in  result[i][1][5]):
                    Elec.ajouterP(float(locale.atof(result[i][3])))
                else:
                    Elec.ajouter(float(locale.atof(result[i][3])))
            if ("OPTIQUE" in  result[i][1]):
                if ("P" in  result[i][1][5]):
                    Optique.ajouterP(float(locale.atof(result[i][3])))
                else:
                    Optique.ajouter(float(locale.atof(result[i][3]))) 
            if ("MECA" in  result[i][1]):
                if ("P" in  result[i][1][5]):
                    # print(result[i])
                    Meca.ajouterP(float(locale.atof(result[i][3])))
                else:
                    # print(result[i])
                    Meca.ajouter(float(locale.atof(result[i][3]))) 
        if (("PROG" in result[i][1][4]) or ("INFO" in result[i][1]) or ("WEB" in result[i][1])):
            # print(result[i][3])
            if ("PROG1" in  result[i][1]):
                if ("P" in  result[i][1][5]):
                    Prog1.ajouterP(float(locale.atof(result[i][3])))
                if ("DS" in  result[i][1][5]):
                    Prog1.ajouterD(float(locale.atof(result[i][3])))
                else:
                    Prog1.ajouter(float(locale.atof(result[i][3])))
            if ("PROG2" in  result[i][1]):
                if ("P" in  result[i][1][5]):
                    Prog2.ajouterP(float(locale.atof(result[i][3])))
                if ("DS" in  result[i][1][5]):
                    Prog2.ajouterD(float(locale.atof(result[i][3])))
                else:
                    Prog2.ajouter(float(locale.atof(result[i][3])))      
            if ("ARDUINO1" in  result[i][1]):
                Arduino.ajouter(float(locale.atof(result[i][3])))       
            if ("PRAT" in  result[i][1]):
                if ("S1" in  result[i][1]):
                    ProgTPS1.ajouter(float(locale.atof(result[i][3])))
                if ("S2" in  result[i][1]):
                    ProgTPS2.ajouter(float(locale.atof(result[i][3]))) 
            if("WEB" in result[i][1]):
                if("S1" in result[i][1]):
                    if ("P" in  result[i][1][5]):
                        WebS1.ajouterP(float(locale.atof(result[i][3])))
                    if ("DS" in  result[i][1][5]):
                        WebS1.ajouterD(float(locale.atof(result[i][3])))
                    else:
                        WebS1.ajouter(float(locale.atof(result[i][3])))
                if("S2" in result[i][1]):
                    if ("P" in  result[i][1][5]):
                        WebS2.ajouterP(float(locale.atof(result[i][3])))
                    if ("DS" in  result[i][1][5]):
                        WebS2.ajouterD(float(locale.atof(result[i][3])))
                    else:
                        WebS2.ajouter(float(locale.atof(result[i][3])))
        if ("ANGLAIS" in result[i][1][4]):
            if ("S1" in result[i][1][3]):
                Anglais1.ajouter(float(locale.atof(result[i][3])))
            if ("S2" in result[i][1][3]):
                Anglais2.ajouter(float(locale.atof(result[i][3])))
        if ("SPORT" in result[i][1][4]):
            if ("S1" in result[i][1][3]):
                Sport1.ajouter(float(locale.atof(result[i][3])))
            if ("S2" in result[i][1][3]):
                Sport2.ajouter(float(locale.atof(result[i][3])))
        if ("COMM" in result[i][1][4]):
            if ("DS" in result[i][1][5]):
                CR.ajouterD(float(locale.atof(result[i][3])))
            else:
                CR.ajouter(float(locale.atof(result[i][3])))
    
    return Maths.moyenne(),Physique.moyenne(),Info.moyenne(),Dev.moyenne()

def main(result):
    resultats = TableNotes.table(result)  #Liste de liste de note sous forme ['07/01/2022', ['2122', 'ISEN', 'CIR1', 'S1', 'WEB', 'P1'], 'Partiel de Technologies Web', ' 16.60', '24']
    
    return rangement(resultats)

# print(main(0,0))
