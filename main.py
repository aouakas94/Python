"""
print('hello ')
nom = input ('ton nom?: ')
age = input ('ton age ? :')
print ('tu t"aappelle ' +nom , 'et tu as ' +age, 'ans')
#-----------------------
"""
""""
nom = 4
prenom= 2
resultat = nom * prenom
resultat = nom + prenom

print (resultat)
one = input ('premier?: ')
two = input ('deuxieme?: ')
resultat = one + two

print (resultat)
"""
""""
-----------------
#one = input ('saisissez: ')
#one = 33
#print (type (one))
nom = 'aouakas'
age =33
# convertir l'age en caractrer pour le concatener 
print ('votre nom est ' +nom , 'et votre age est ' + str(age))
nom = input ('str')
-----------------
"""
"""
one = input('saissaissez un nombre ')
#operation= input('saisir operation')
two = input('saissaissez un autre ')
resultat = int(one) + int(two)
try:
    resultat = int(one) * int(two)
except ValueError:
    print("erreur")
else:
    print (resultat)
"""
#boucle while
"""
n=8
#print(n)
#n=n+1
#print(n)

while n <= 10
    print(n)
    n = n + 1
"""
"""
#if
#nom = input('nom?:')
mot_de_passe = input('mot de passe?:')

while not mot_de_passe == "aouakas":
        mot_de_passe = input('mot de passe erroné resaissez le:')
print('azul aouakas')
# video 27 debugeur a revoir


#demander le nom pas vide
nom = ""
nom = input('nom?:')
while nom == "":
    nom = input('inser un nom?:')
print("bonjour " + nom)
"""

#fonction





def demande_age():
    age_int = 0
    while age_int == 0:
        age_str = input("quel est votre age? :")
        try:
            age_int = int(age_str)
        except:
            print("error entrez un nombre reel ")
    return age_int


nom = ""
while nom == "":
    nom = input('inserez un nom?:')
age = demande_age()

print ("bonjour " + nom )
print ("vous avez " + str(age) + " ans")
print ("lannée prochaine vous aurez " + str(age+1) + " ans")






 