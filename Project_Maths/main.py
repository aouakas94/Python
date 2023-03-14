import random
NOMBRE_MIN=1
NOMBRE_MAX=10
NB_QUESTIONS=5


def poser_question():
    a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    reponse_str=input(f"calculer {a} + {b} = ")
    reponse_int=int( reponse_str)
    if reponse_int == a+b:
        return True
    
    return False

    

NB_POINT=0

for i in range(0, NB_QUESTIONS):
    print(f"question n° {i+1} sur {NB_QUESTIONS}:")
    if poser_question():
        print("reponse correcte")
        NB_POINT += 1
    else:
        print("reponse incorrecte")
print(f"votre note est :  {NB_POINT}/{NB_QUESTIONS}")
        
    #poser_question()



        
    
    