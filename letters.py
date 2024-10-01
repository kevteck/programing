letters=["a", "b", "c", "d", "e", "f", "g", "h", "j", "n" ]



ord = input ()


for x in ord:
    for y in letters: 
        if y == x:
            letters.remove(x)

print(letters)
