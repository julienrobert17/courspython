# coding: utf-8

#sert à lire le fichier data.txt
def lire():
    fichier = open('data.txt', 'r')
    print (fichier.readlines())
    fichier.close

#sert à écrire dans le fichier data.txt
def ecrire():
    fichier = open("data.txt", "a")
    fichier.write('\nbonjour')
    fichier.close  
    
__name__="__main__"
    
ecrire()    
lire()

print(type(pythonexercice1))