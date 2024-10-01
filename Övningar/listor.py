länder = ["norge", "danmark", "sverge",  "finland",  "spain" ]
for x in länder:
  print(x, "är", len(x), "vokaler")



vokaler = ["a", "o", "i", "e" ]

ordet = input().lower()

antal_vokaler = 0

for bokstav in ordet:
  if bokstav in vokaler:
    antal_vokaler +=1


print(antal_vokaler)
