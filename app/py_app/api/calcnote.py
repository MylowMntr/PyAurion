from getnotes import main
from HtmlToDict import table 

result = main()
result = table(result)

Notes = []
Coefs = []
for i in range (len(result)):
    Notes.append(result[i][3])
    Coef.append(result[i][4])
    
    
#moyenne a partir d'une liste de note du module
def Moyenne(Notes, Coefs):
    for g in range(len(Notes)):
        Notes[g] = Notes[g] * Coefs[g] / sum(Coefs)
    moy =  sum(Notes)
    return moy

  
# Notes = [ 10, 4, 7, 12, 9 ]
# amount = [3, 2, 2, 12, 1] 
print(Moyenne(Notes, Coefs))

