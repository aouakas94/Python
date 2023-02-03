def demande_nom():
    nom = ""
    while nom == "":
          nom = input('inserez un nom?:')
    print ("bonjour " +nom)
    return nom

def demande_age(personne):
    age = 0
    while age== 0:
        age = input(personne +' quel est votre age?: ')
    print ("vous avez "+ age)
    return age

nom1=demande_nom()
nom2=demande_nom()

age1=demande_age(nom1)
age2=demande_age(nom2)

print(nom1)
print(nom2)

print(age1)
print(age2)

#nom1=demande_nom()
#nom2=demande_nom()










 