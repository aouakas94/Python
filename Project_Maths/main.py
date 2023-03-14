import random
NOMBRE_MIN=1
NOMBRE_MAX=10

def poser_question():
    a = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN,NOMBRE_MAX)
    reponse_str=input(f"calculer {a} + {b} = ")
    reponse_int=int( reponse_str)
    if reponse_int == a+b:
        print("reponse corecte")
    else:
        print("reponse incorecte")
poser_question()
        
    
    