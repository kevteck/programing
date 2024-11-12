import random

alternativ = ["sten", "sax", "påse"]

spelar_poäng = 0
dator_poäng = 0

while spelar_poäng < 3 and dator_poäng < 3:

    spelar_val = input()
    dator_val = random.choice(alternativ)

    if spelar_val == "sten" and dator_val == "sten":
        print("oavgjort")
    if spelar_val == "sten" and dator_val == "sax":
        print("spelar_van")
        spelar_poäng += 1
    if spelar_val == "sten" and dator_val == "påse":
        print("dator_van") 
        dator_poäng += 1 
    if spelar_val == "sax" and dator_val == "sten":
        print("dator_van")
        dator_poäng += 1
    if spelar_val == "sax" and dator_val == "sax":
        print("oavgjort")
    if spelar_val == "sax" and dator_val == "påse":
        print("spelare_van")
        spelar_poäng += 1
    if spelar_val == "påse" and dator_val == "sten":   
        print("spelar_van")
        spelar_poäng += 1
    if spelar_val == "påse" and dator_val == "sax":
        print("dator_van") 
        dator_poäng += 1
    if spelar_val == "påse" and dator_val == "påse":    
        print("oavgjort")
    print(dator_val)




print("dator_van," "skillissukid," "getgood")

print("spelar_van," "do btter win more" )