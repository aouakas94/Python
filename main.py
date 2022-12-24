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
one = input('saissaissez un nombre ')
#operation= input('saisir operation')
two = input('saissaissez un autre ')
resultat = int(one) + int(two)
try:
    resultat = int(one) + int(two)
except ValueError:
    print("erreur")
else:
    print (resultat)



