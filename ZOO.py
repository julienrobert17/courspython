class animals :
    
    def __init__(self, alimentation, nbdepatte, qtdenourriture, domestique):
        self.alimentation = alimentation
        self.qtdenourriture = qtdenourriture
        self.domestique=domestique
        self.nbdepatte = nbdepatte
    
    def __str__(self):
        return " est un "+self.alimentation+" il a "+str(self.nbdepatte)+" de pattes, et il mange "+str(self.qtdenourriture)+"g de nourriture, il "+self.domestique+" domestique"
        
class mammifère(animals):
        
    def __str__(self):
        return " est un "+self.alimentation+" il a " +str(self.nbdepatte)+ " pattes et il mange "+str(self.qtdenourriture)+"g de nourriture, il "+self.domestique+" domestique"
       
class marin(animals):
    pass

'''def qtnourriture():
    for my_key in le_zoo:
       maxfood = le_zoo[qtdenourriture]
        
    return maxfood'''
    
    
if __name__=="__main__":
    
    
    le_zoo={}
    
    le_zoo["Humain"]=mammifère("omnivore", 2, 600, "n'est pas")
    
    le_zoo["Lion"]=mammifère("omnivore", 4, 3000, "n'est pas")
    
    le_zoo["Lapin"]=mammifère("végétarien",4, 100, "est")
    
    le_zoo["Mouton"]=mammifère("végétarien", 4, 500, "est")
    
    le_zoo["Chien"]=mammifère("omnivore", 4, 500, "est")
    
    le_zoo["Pieuvre"]=marin("carnivore", "pas", 200, "n'est pas")
   
    le_zoo["Serpent"]=animals("carnivore", "pas", 200, "n'est pas")
    
    le_zoo["Autruche"]=animals("omnivore", 2, 1000, "n'est pas")
    
    le_zoo["Poule"]=animals("omnivore", 2, 200, "est")
    
    for my_key in le_zoo:
        print(my_key+""+str(le_zoo[my_key]))
        maxnourriture = maxnourriture + le_zoo[my_key].qtdenourriture
    
    print("il faut "+str(maxnourriture)+" g par jour")
    
    