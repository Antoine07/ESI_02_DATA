# 1 classique 

def mult(l, m):
    assert len(l) == len(m)

    s = 0
    for i in range(0, len(l)):
        s += l[i] * m [i]

    return s 


# 2 Pythonique 

def multZip(l, m):
    assert len(l) == len(m)

    return sum( x * y for x, y in zip( l, m ) )

print( mult([1,2], [3, 4]) )
print( multZip([1,2], [3, 4]) )