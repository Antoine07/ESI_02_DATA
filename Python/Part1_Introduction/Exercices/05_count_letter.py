# 1 avec un set et une fonction spécialisée

m = "mississippi" 

def countLetter(letter, message):
    count = 0
    for m in message :
        if letter.lower() == m.lower() : 
            count += 1

    return count 

print(countLetter("I", m) )

s = { letter : countLetter(letter, m) for letter in set(m) }
print(s)

# 2 avec la fonction count et un set

m = "mississippi" 
s = { l : m.count(l) for l in set(m) }
print(s)

