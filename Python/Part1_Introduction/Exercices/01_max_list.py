l = [0, 1, 100, 4, 9, 16, 25, 36, 49, 64, 81]   

# 1

# m, j = l[0], 0  # syntaxe plus rapide pour initialiser les variables
m = l[0] 
j = 0
for i in range(1, len(l)) :
    if l[i] > m :
        m = l[i]  # m, j = l[i], i
        j = i 

print(f"Max : {m} à l'indice : {j}")

# 2 

def maxList(l):
    m, j = l[0], 0
    for i in range(1, len(l)) :
        if l[i] > m :
            m, j = l[i], i
    
    return m, j

print(maxList(l))