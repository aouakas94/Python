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
            print("reponse corecte")
        else:
            print("reponse incorecte")


for i in range(0, NB_QUESTIONS):
    print(f"question n° {i+1} sur {NB_QUESTIONS}:")
    poser_question()
        
    
    