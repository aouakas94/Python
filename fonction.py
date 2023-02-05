
def demande_nom():
    nom = ""
    while nom == "":
          nom = input('inserez un nom?:')
    print ("bonjour " +nom)
    return nom

def demande_age(param1):
    age_int = 0
    while age_int== 0:
        age_str = input(param1 +' quel est votre age?: ')
        try:
            age_int = int(age_str) 
        except ValueError:
            print ("error ")
    #print ("vous avez "+ age)

    condition= age_int >= 18
    if condition:
        print("vous etes majeur ")
    else:
       print("mineur lol")

    return age_int
'''
nom1=demande_nom()
nom2=demande_nom()

age1=demande_age(nom1)
age2=demande_age(nom2)

#print(nom1)
#print(nom2)

#print(age1)
#print(age2)

#nom1=demande_nom()
#nom2=demande_nom()


#fonction a 2 params

def demande_info(nom,age):
    print("bonjour " +nom + " vous avez " + str(age) + " ans")
    if age >= 18:
            print("vous etes majeur ")
    elif age>=12 and age <18:
        print("adolesent lol")
    elif age<3 and age <18:
        print("mineur et bebe haha")
   

demande_info(nom1,age1)
demande_info(nom2,age2)
'''

#boucle for
for i in range(0,5):
    nom="personne" + str(i+1)
    demande_age(nom)
    














 