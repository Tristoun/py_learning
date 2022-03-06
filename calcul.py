from random import randint
"""Faire une petite classe joueur"""
class Calcul () :
    def __init__(self, life = 3):
        """Initialise l'objet"""
        self.lst_nb = []
        self.nb_number = int(input("Cb de nombre : "))
        self.result = 0
        self.affichage = ""
        self.symbole = 0
        self.boucle = 0
        self.life = life
    
    def est_premier (self, k) :
        if k > 1:
            for i in range(2, int(k/2)+1):
                if (k % i) == 0:
                    return False       
            else:
                return True
        else:
            return False

    def reset (self) :
        """Renitialise le calcul pour en créer un nouveau"""
        self.result = self.lst_nb[0]
        self.affichage = str(self.lst_nb[0])
        self.boucle = 0
        del self.lst_nb[0]

    def init_para (self) :
        self.lst_nb.clear()
        if self.boucle == 0 :
            self.symbole = randint (1,4)
            self.boucle = 1
        for i in range (self.nb_number) :
            self.lst_nb.append (randint(1, 10))

    def create (self) :
        self.init_para()
        if self.symbole == 1 :
            res = self.add()
        elif self.symbole == 2 :
            res = self.sub()
        elif self.symbole == 3 :
            res = self.mult()
        elif self.symbole == 4 :
            res = self.div()
            while int(self.result) != self.result :
                    self.init_para()
                    res = self.div()
        else :
            return "error"
        return self.affi(res)

    def add (self) :
        """Addition"""
        assert (self.lst_nb != [])
        self.reset()
        for i in range (len(self.lst_nb)) :
            self.result += self.lst_nb[i]
            self.affichage += " + " + str(self.lst_nb[i]) 
        return self.affichage

    def sub (self) :
        """Soustraction"""
        self.reset()
        for i in range (len(self.lst_nb)) :
            self.result -= self.lst_nb[i]
            self.affichage += " - " + str(self.lst_nb[i]) 
        return self.affichage


    def mult (self) :
        """Multiplication"""
        self.reset()
        for i in range (len(self.lst_nb)) :
            self.result *= self.lst_nb[i]
            self.affichage += " X " + str(self.lst_nb[i]) 
        return self.affichage

    def div (self) :
        """Division"""
        self.reset()
        for i in range (len(self.lst_nb)) :
            self.result /= self.lst_nb[i]
            self.affichage += " / " + str(self.lst_nb[i]) 
        return self.affichage

    def affi (self, res) :
        print (res)
        j_res = float(input("Résultat : "))
        if j_res == self.result :
            return True 
        else :
            print (self.result)
            return False

    def game (self) :
        score = 0
        while self.life != 0 :
            vrai_faux = c.create()
            if vrai_faux == False :
                self.life -=1
            else :
                score += 1
        return score

                
c = Calcul()
print (c.game())

