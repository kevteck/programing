import random

ja = ["ja", "okej"]

otydlight = [ "öl", "gurka"]

nej = ["va fan", "jag hatar makor"]
    


val = random.randint(1,3)

if val == 1:
    print(random.choice(ja))
elif val == 2:
    print(random.choice(otydlight))
else:
    print(random.choice(nej))


