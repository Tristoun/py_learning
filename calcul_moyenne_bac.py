coefbac = {'Francais' : 10, 'Philosophie' : 8, 'Spe1' : 16, 'Spe2' : 16, 'Spe3' : 5, 'HG' : 5, 'LV1' : 5, 'LV2' : 5, 'ES': 5} #coefficient des matières au bac

coef_n = {'ds' : 2, 'td' : 1, 'oral' : 0.5, 'tp' : 0.5, 'exposé' : 1} #coefficient des différents travaux dans les matières


'''
:n_francais: est une liste regroupant toutes les notes de francais et leurs coefficients
Idem pour les autres liste 
'''
n_Francais = []
n_philo = []
n_Spe1 = []
n_Spe2 = []
n_Spe3 = []
n_HG = []
n_LV1 = []
n_LV2 = []
n_ES = []

'''
:lst_mat: liste regroupant toutes les matières
:lst_travaux: liste regroupant tout les types de devoirs possibles
'''
lst_mat = ['Francais', 'Philosophie', 'Spe1', 'Spe2', 'Spe3', 'HG', 'LV1', 'LV2', 'ES']
lst_travaux = ['ds','tp', 'td', 'oral', 'exposé']

def bac(calculmoyenne) :
    '''
    Calcul la mention au  bac
    '''
    if calculmoyenne > 16 :
        return "Mention TB"
    elif calculmoyenne > 14 :
        return "Mention B"
    elif calculmoyenne > 12 :
        return "Mention AB"
    else :
        return 'Pas de mention'

def calculmoyenne() :
    '''
    Calcul la moyenne général et donc la moyenne au bac de l'élève, utilise la fonction "calcul_mat()"
    moymat, moymat2, coeffmat2, coeffmat : sont des entiers permettant de calculer la moyenne grâce au coefficient et au note

    '''
    listevariablenote = [n_Francais, n_philo, n_Spe1, n_Spe2, n_Spe3, n_HG,n_LV1, n_LV2, n_ES]
    moymat = 0
    moymat2 = 0
    coeffmat2 = 0
    coeffmat = 0
    for i in range (len(listevariablenote)) :
        if len(listevariablenote[i]) == 0 :
            pass
        else :
            moymat = calcul_mat(listevariablenote[i])
            coeffmat = coefbac[lst_mat[i]]
            moymat = moymat * coeffmat
            coeffmat2 += coeffmat
            moymat2 += moymat
    if coeffmat == 0 : #vérifie si au moins une note a été au moins ajoutée
        return "`\nAjoutez au moins une valeur" 
    return moymat2/coeffmat2


def calcul_mat (ls_notetrav) :
    '''
    Calcul la moyenne d'une matière
    '''
    calculn = 0
    calculco = 0
    listenote = []
    listecoeff  = []
    for i in range (len(ls_notetrav)) :
        listenote.append(ls_notetrav[i][0])
        listecoeff.append(coef_n[ls_notetrav[i][1]])
    for j in range (len(listenote)) :
        calculn += listenote[j] * listecoeff[j]
        calculco += listecoeff[j]
    return calculn/calculco


def question() :
    '''
    Pose une question à l'utilisateur pour ensuite calculer la moyenne de la matière désirer
    '''
    qmatiere = str(input("De qu'elle matière voulez vous calculez la moyenne : "))
    if qmatiere in lst_mat :
        if qmatiere == 'Francais' :
            piou = calcul_mat(n_Francais) #Appele la fonction calcul_mat à travers la variable piou en y faisant passer la variable avec les notes de la matière demandée
        elif qmatiere == 'Philosophie' :
            piou = calcul_mat(n_philo)
        elif qmatiere == 'Spe1' :
            piou = calcul_mat(n_Spe1)
        elif qmatiere == 'Spe2' :
            piou = calcul_mat(n_Spe2)
        elif qmatiere == 'Spe3' :
            piou = calcul_mat(n_Spe3)
        elif qmatiere == 'HG' :
            piou = calcul_mat(n_HG)
        elif qmatiere == 'LV1' :
            piou = calcul_mat(n_LV1)
        elif qmatiere == 'LV2' :
            piou = calcul_mat(n_LV2)
        elif qmatiere == 'ES' :
            piou = calcul_mat(n_ES)
    else :
        return "ERREUR" #Retourne une Erreur si la matière demandé n'existe pas
    return piou

def ajouterNote() :
    '''
    Ajoute une note à la variable de la matière demandée
    '''
    print ("\nLes matières disponibles sont : ", lst_mat)
    matiere = str(input("\nVeuillez indiquez la matière de la note : "))
    if matiere in lst_mat : #vérifie si la matière demandée existe sinon retourne une erreur
        print ("\nLes travaux disponibles sont : ", lst_travaux)
        trav = str(input("\nQuel type de travail ? : "))
        if trav in lst_travaux : #vérifie si le type de travail demandé existe sinon retourne une erreur
            try :
                note = int(input("Veuillez entrez une note : "))  #test si la note entrée est bien un entier sinon retourne une erreur
            except ValueError :
                return "ERREUR"

            if trav in lst_travaux :
                if matiere == 'Francais' :
                    n_Francais.append((note, trav))
                elif matiere == 'Philosophie' :
                    n_philo.append((note, trav))
                elif matiere == 'Spe1' :
                    n_Spe1.append((note, trav))
                elif matiere == 'Spe2' :
                    n_Spe2.append((note, trav))
                elif matiere == 'Spe3' :
                    n_Spe3.append((note, trav))
                elif matiere == 'HG' :
                    n_HG.append((note, trav))
                elif matiere == 'LV1' :
                    n_LV1.append((note, trav))
                elif matiere == 'LV2' :
                    n_LV2.append ((note, trav))
                elif matiere == 'ES' :
                    n_ES.append ((note, trav))
            else : 
                return "ERREUR"
        else :
            return "ERREUR"
    else: 
        return "ERREUR"

def main() :
    '''
    Fonction principal du programme marche comme un menu affichant le menu en permanence
    '''
    while True :
        try :
            n = int(input("\nQue vous voulez vous faire :\n1-Ajoutez une note\n2-Calculer la moyenne d'une matière\n3-Calculer la moyenne et la mention au bac\n4-quitter le programme\nEntrez un nombre en fonction de l'action souhaitez : ")) 
        except ValueError:
            print ("\nOups... le nombre entier ne correspond à aucune commande\n")
            main()
        if n == 4 :
            quit()
        elif n == 1 :
            print(ajouterNote()) 
        elif n == 2 :
            piou2 = question()
            print ("\nVotre moyenne est de : ",piou2)
        elif n == 3 :
            print("\n Votre moyenne général est de  : ",calculmoyenne())
            bac(calculmoyenne)


main()
